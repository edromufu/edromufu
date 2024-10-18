
#include <Arduino.h>
#include <esp_now.h>
#include <micro_ros_arduino.h>
#include <WiFi.h>
// MicroROS Libraries
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
//#include <potmessage/msg/imumsg.h>
//#include <potmessage/msg/buttonmsg.h>
#include <std_msgs/msg/float32_multi_array.h>

// MicroROS Variaveis
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;
rcl_publisher_t publisher;
rcl_publisher_t publisher2;
rcl_subscription_t subscriber;

// !!! Não precisamos mais das mensagens customizadas !!!
std_msgs__msg__Float32MultiArray feedbackMsg;
std_msgs__msg__Float32MultiArray msg;

//potmessage__msg__Imumsg msgImu;
//potmessage__msg__Buttonmsg msgBot;
// ------------------------------------

esp_now_peer_info_t peerInfo;

int potPrint[8];
int numPorts=8;

//============== ESPNOW ================
typedef struct struct_message {
  uint16_t potValue[8];
} struct_message;
struct_message myData;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));
}
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
//--------constantes Graus--------
float atualPos[8];
const int pot_size = 8;


//--------constantes Drivers-------- ****TEM QUE PEGAR TUDO DO DIAGRAMA DA ELÉTRICA!!!!!!!****
const int ACTUATOR_EN_PINS[] =     {34, 27, 33, 13, 1, 2, 19, 17}; //vetor de PWM
const int ACTUATOR_IN_IMP_PINS[] = {39, 26, 32, 12, 22, 4, 21, 5}; //vetor de pino de avanço
const int ACTUATOR_IN_PAR_PINS[] = {36, 25, 35, 14, 23, 16, 3, 18}; //vetor de pino de recuo

//--------constantes PID--------
const float Kp[] =  {10, 10, 10, 10, 10, 10, 10, 10};
const float Ki[] =  {0, 0, 0, 0, 0, 0, 0, 0};
const float Kd[] =  {0, 0, 0, 0, 0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0, 0, 0, 0, 0};
float accError[] =  {0, 0, 0, 0, 0, 0, 0, 0};
float data[] =      {0, 0, 0, 0, 0, 0, 0, 0};   //Ângulos a serem recebidos por ROS da cinemática inversa
int u_input[] =     {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de PWM a ser aplicado nos atuadores
int dt = 1000;                                  // tempo de amostragem em milisegundos


void initJoint(int id){
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_IMP_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_PAR_PINS[id], OUTPUT);
}

// --------- Funçoes ---------

void initJoint(int id){
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_IMP_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_PAR_PINS[id], OUTPUT);
}


int calculatePID(int id, int setpoint, float current){
  float erro = setpoint - current;

  float derro = 1000*(erro - lastError[id])/dt;
  
  accError[id]+= erro*dt/1000;

  int u = Kp[id]*erro +Ki[id]*accError[id]+ Kd[id]*derro;
  return u;
}


void writeActuator (int id, int signal){
  // Pega o valor de u fornecido pelo PID e transforma em comandos para os drivers
  // id: id da junta
  // signal: valor de -10000 10000 para escrever na junta
  int newSignal = constrain(signal, -10000, 10000);
  newSignal = 255*newSignal/10000; // olhar o 255
  if (signal >= 0){
    digitalWrite(ACTUATOR_IN_IMP_PINS[id], HIGH);
    digitalWrite(ACTUATOR_IN_PAR_PINS[id], LOW);
    analogWrite(ACTUATOR_EN_PINS[id], newSignal);
  }
  if (signal < 0){
    digitalWrite(ACTUATOR_IN_IMP_PINS[id], LOW);
    digitalWrite(ACTUATOR_IN_PAR_PINS[id], HIGH);
    analogWrite(ACTUATOR_EN_PINS[id], -newSignal);
  }
}


// =====================================

float pot2Degrees(float value){
  //float factor = 90/1384; //0.06502
  float factor = 0.06491; //0.06491
  return value*factor;
}

float feedbackData[8];

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }

  if (esp_now_init() != ESP_OK) return;

  esp_now_register_recv_cb(esp_now_recv_cb_t(OnDataRecv));

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
  RCCHECK(rclc_publisher_init_default(&publisher,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs ,msg, Float32MultiArray),"pot_topic"));
  RCCHECK(rclc_publisher_init_default(&publisher2,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32MultiArray),"pot_feedback_topic"));
  RCCHECK(rclc_subscription_init_default(&subscriber,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32MultiArray),"pot_py_topic"));

  // create timer,
  const unsigned int timer_timeout = 1000;
  RCCHECK(rclc_timer_init_default(
    &timer,
    &support,
    RCL_MS_TO_NS(timer_timeout),
    timer_callback));


  // create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 3, &allocator));
  RCCHECK(rclc_executor_add_timer(&executor, &timer));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &feedbackMsg, &subscription_callback, ON_NEW_DATA));

  msg.data.capacity = 8;  // Size of your array
  msg.data.size = 8;
  feedbackMsg.data.data = (float *) malloc(8 * sizeof(float));
  feedbackMsg.data.size = 8;
  feedbackMsg.data.capacity = 8;
}

void loop() {
  unsigned long now = millis();

  for (size_t i = 0; i < 8; i++) {
    data[i] = (float)pot2Degrees(myData.potValue[i]); 
  }
  
  msg.data.data = data;

  RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
  while (millis()-now<dt){
    // now = millis();
  }
  
    //--------Calculando Saídas dos PID's--------
  for (int i = 0; i < pot_size; i++){
    u_input[i] = calculatePID(i , data[i], atualPos[i]);
  }
  


  //--------Calculando Entrada do PWM--------
  writeActuator(0, u_input[1]+u_input[0]); //Tem que ver
  writeActuator(1, u_input[1]-u_input[0]);
  
  writeActuator(2, u_input[2]+u_input[3]);
  writeActuator(3, u_input[2]-u_input[3]);
  
  writeActuator(4, u_input[5]+u_input[4]);
  writeActuator(5, u_input[5]-u_input[4]);
  
  writeActuator(6, u_input[6]+u_input[7]);
  writeActuator(7, u_input[6]-u_input[7]);
  

}

void subscription_callback(const void * msgin)
{  
  const std_msgs__msg__Float32MultiArray * feedback = (const std_msgs__msg__Float32MultiArray *)msgin;

  for(int i = 0; i < 8; i++){
    feedbackData[i] = pot2Degrees(feedback->data.data[i]);
  }

  feedbackMsg.data.data = feedbackData;

  RCSOFTCHECK(rcl_publish(&publisher2, &feedbackMsg, NULL));

}
