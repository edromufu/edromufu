#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
#include <micro_ros_arduino.h>
#include <rcl/rcl.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/float32.h>
#include <std_msgs/msg/float32_multi_array.h>

// Usado no Subscriber
rcl_subscription_t subscriber;
rclc_executor_t executor;
std_msgs__msg__Float32MultiArray potmsg;
// Usado no Publisher de Feedback
std_msgs__msg__Float32 msg;
rcl_publisher_t publisher;
rclc_executor_t executor2;

// Usado no MicroROS
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;

// ------- Declaração de pinos -------
#define LED_PIN 13
const int POT_PINS[] = {34, 35, 32, 33}; // vetor de portas de potenciômetros
const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; // vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; // vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; // vetor de pino de recuo
const int pot_size = 4; // número de juntas

// -------- Variáveis ----------
int pot_values[pot_size]; // valores lidos na junta
const int n_size = 15; // quantidade de média móvel

// -------- Constantes PID --------
const float Kp[] = {10, 10, 10, 10};
const float Ki[] = {0, 0, 0, 0};
const float Kd[] = {0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0};
float accError[] = {0, 0, 0, 0};
float angles[] = {0, 0, 0, 0, 0, 0, 0, 0};
int dt = 1000; // tempo de amostragem em milisegundos

// ESP-NOW variáveis
typedef struct struct_message {
  uint16_t potValue[8];
} struct_message;
struct_message myData;

// ------- ros2 ----------
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

void error_loop(){
  while(1){
    delay(100);
  }
}

// Callback do publisher de feedback
void timer_callback(rcl_timer_t * timer, int64_t last_call_time) {  
  RCLC_UNUSED(last_call_time);
  if (timer != NULL) {
    RCSOFTCHECK(rcl_publish(&publisher, &msg, NULL));
  }
}

// RECEBE OS DADOS AQUI
void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));
  // Recebe os valores dos pot e coloca todos nesse vetor

  for (int i = 0; i < 8; i++) {
    potmsg.data.data[i] = myData.potValue[i];
  }
  potmsg.data.size = 8;

}

void writeActuator(int id, int signal) {
  // id: id da junta
  // signal: valor de -10000 10000 para escrever na junta
  int newSignal = constrain(signal, -10000, 10000);
  newSignal = 255 * newSignal / 10000;
  if (signal >= 0) {
    digitalWrite(ACTUATOR_INA_PINS[id], HIGH);
    digitalWrite(ACTUATOR_INB_PINS[id], LOW);
    analogWrite(ACTUATOR_EN_PINS[id], newSignal);
  }
  if (signal < 0) {
    digitalWrite(ACTUATOR_INA_PINS[id], LOW);
    digitalWrite(ACTUATOR_INB_PINS[id], HIGH);
    analogWrite(ACTUATOR_EN_PINS[id], -newSignal);
  }
}

void initJoint(int id) {
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INA_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INB_PINS[id], OUTPUT);
}

int calculatePID(int id, int setpoint, float current) {
  float erro = setpoint - current;
  float derro = 1000 * (erro - lastError[id]) / dt;
  accError[id] += erro * dt / 1000;
  int u = Kp[id] * erro + Ki[id] * accError[id] + Kd[id] * derro;
  return u;
}

void setup() {
  Serial.begin(115200);
  
  // Inicializar ESP-NOW
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) return;
  esp_now_register_recv_cb(OnDataRecv);

  // Configurar endereço MAC do transmissor ESP1
  uint8_t broadcastAddress[] = {"Tava sem esp"};  //pega o endereço MAC do mini esp
  esp_now_peer_info_t peerInfo;
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }

  // Inicializar micro-ROS
  set_microros_transports();
  delay(100);
  allocator = rcl_get_default_allocator();
  
  // create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_arduino_node", "", &support));
  
  // create publisher de feedback
  RCCHECK(rclc_publisher_init_default(
    &publisher,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),
    "feedback"));
  
  // create timer de feedback
  const unsigned int timer_timeout = 1000;
  RCCHECK(rclc_timer_init_default(
    &timer,
    &support,
    RCL_MS_TO_NS(timer_timeout),
    timer_callback));

  // create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  
  // Executor do publisher de feedback
  RCCHECK(rclc_executor_init(&executor2, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_timer(&executor2, &timer));

  // Inicializar potmsg data array
  potmsg.data.data = (float*) malloc(8 * sizeof(float));
  potmsg.data.capacity = 8;

  // Inicializar juntas
  for (int i = 0; i < pot_size; i++) {
    initJoint(i);
  }
}

void loop() {
  // Processar os dados recebidos e executar o controle PID
  for (int i = 0; i < pot_size; i++) {
    float current_value = potmsg.data.data[i]; // Usar dados recebidos via ESP-NOW
    int setpoint = 1000; // Definir seu setpoint desejado
    int control_signal = calculatePID(i, setpoint, current_value);
    writeActuator(i, control_signal);
  }

  RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
}
