
#include <Arduino.h>
#include <esp_now.h>
#include <micro_ros_arduino.h>
#include <WiFi.h>
// MicroROS Libraries
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <potmessage/msg/potmsg.h>
#include <potmessage/msg/imumsg.h>
#include <potmessage/msg/buttonmsg.h>

// MicroROS Variaveis
rclc_executor_t executor;
rclc_executor_t executor2;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_allocator_t allocator2;
rcl_node_t node;
rcl_timer_t timer;
rcl_publisher_t publisher;
rcl_subscription_t subscriber;
potmessage__msg__Potmsg msg;
potmessage__msg__Potmsg msg2;
potmessage__msg__Imumsg msgImu;
potmessage__msg__Buttonmsg msgBot;
// ------------------

esp_now_peer_info_t peerInfo;

int potPrint[8];
int numPorts=8;

//============== ESPNOW ================
typedef struct struct_message {
  uint16_t potValue[8];
} struct_message;
struct_message myData;

void onDataReceived(const uint8_t * mac, const uint8_t* incomingData, int len);
//======================================

//============== MicroROS ==============
#define RCCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) { error_loop(); } \
  }
#define RCSOFTCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) {} \
  }
void error_loop() {
  Serial.println("ERROR LOOP");
}
void timer_callback(rcl_timer_t* timer, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer != NULL) {
    RCSOFTCHECK(rcl_publish(&publisher, &msg, NULL));
  }
}
//======================================

// ================ PID ================
//------- Pinos -------
#define LED_PIN 13
const int POT_PINS[] = {34, 35, 32, 33}; // vetor de portas de potenciômetros
const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; //vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; //vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; //vetor de pino de recuo
const int pot_size = 4; //número de juntas
//---------- Variaveis ----------
int pot_values[pot_size]; // valores lidos na junta
const int n_size = 15; // quantidade de média móvel
//-------- Constantes PID --------
const float Kp[] = {10, 10, 10, 10};
const float Ki[] = {0, 0, 0, 0};
const float Kd[] = {0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0};
float accError[] = {0, 0, 0, 0};
float angles[] = {0, 0, 0, 0, 0, 0, 0, 0};
int dt = 1000; // tempo de amostragem em milisegundos
// --------- Funçoes ---------
float readJoint(int id){
  // THIS IS JUST AVERAGE
  // TODO: implement moving average
  double acc = 0;
  for (int i = 0; i<n_size; i++){
    acc+= analogRead(POT_PINS[id]);
  }
  acc = acc/(n_size*1.0);
  float degrees = acc;//0.0699*acc-143.775;
  return degrees;
}

void writeActuator (int id, int signal){
  // id: id da junta
  // signal: valor de -10000 10000 para escrever na junta
  int newSignal = constrain(signal, -10000, 10000);
  newSignal = 255*newSignal/10000;
  if (signal >= 0){
    digitalWrite(ACTUATOR_INA_PINS[id], HIGH);
    digitalWrite(ACTUATOR_INB_PINS[id], LOW);
    analogWrite(ACTUATOR_EN_PINS[id], newSignal);
  }
  if (signal < 0){
    digitalWrite(ACTUATOR_INA_PINS[id], LOW);
    digitalWrite(ACTUATOR_INB_PINS[id], HIGH);
    analogWrite(ACTUATOR_EN_PINS[id], -newSignal);
  }
}

void initJoint(int id){
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INA_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INB_PINS[id], OUTPUT);
}

int calculatePID(int id, int setpoint, float current){
  float erro = setpoint - current;
  float derro = 1000*(erro - lastError[id])/dt;
  
  accError[id]+= erro*dt/1000;

  int u = Kp[id]*erro +Ki[id]*accError[id]+ Kd[id]*derro;
  return u;
}
// =====================================

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }

  if (esp_now_init() != ESP_OK) return;

  esp_now_register_recv_cb(onDataReceived);

  uint8_t broadcastAddress[] = {0x70, 0x04, 0x1D, 0x91, 0x62, 0xF8}; 
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
  set_microros_transports();
  delay(300);

  allocator = rcl_get_default_allocator();

  //create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_pot_node", "", &support));

  // create publisher
  RCCHECK(rclc_publisher_init_default(&publisher,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(potmessage ,msg, Potmsg),"pot_topic"));
  RCCHECK(rclc_subscription_init_default(&subscriber,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(potmessage, msg, Potmsg),"pot_sub"));

  // create timer,
  const unsigned int timer_timeout = 1000;
  RCCHECK(rclc_timer_init_default(
    &timer,
    &support,
    RCL_MS_TO_NS(timer_timeout),
    timer_callback));

  // create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
  RCCHECK(rclc_executor_add_timer(&executor, &timer));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &msg2, &subscription_callback, ON_NEW_DATA));

}

void loop() {
  unsigned long now = millis();

  Serial.print("Potentiometer Value: ");
  for (int i = 0; i < numPorts; i++){
      potPrint[i] = myData.potValue[i];
    Serial.print(String(potPrint[i]) + " ");
    }
  Serial.println("Receiver");

  msg.pot1 = myData.potValue[0];
  msg.pot2 = myData.potValue[1];
  msg.pot3 = myData.potValue[2];
  msg.pot4 = myData.potValue[3];
  msg.pot5 = myData.potValue[4];
  msg.pot6 = myData.potValue[5];
  msg.pot7 = myData.potValue[6];
  msg.pot8 = myData.potValue[7];

  RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
  while (millis()-now<dt){
    // now = millis();
  }
}

void onDataReceived(const uint8_t * mac, const uint8_t* incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(struct_message));
}

void subscription_callback(const void * msgin)
{  
  const potmessage__msg__Potmsg * msg2 = (const potmessage__msg__Potmsg *)msgin;
}