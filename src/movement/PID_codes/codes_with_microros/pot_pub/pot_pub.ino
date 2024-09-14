#include <micro_ros_arduino.h>

#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/float32_multi_array.h>
#include <potmessage/msg/potmsg.h>
#include <buttonmessage/msg/buttonmsg.h>

rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;

//const int POT_PINS[] = {0}; // Tem que configurar os pinos (mudar pra oito)
const int pot_size = 8;    // Mudar pra 8
int pot_values[pot_size];  // valores lidos na junta
const int n_size = 15;     // quantidade de média móvel

//---------Mux----------------
const int addMux = 0x20;
const int pinSaidaMux = 0;
const int pinS0 = 2;
const int pinS1 = 3;
const int pinS2 = 4;
//----------------------------

rcl_publisher_t publisher;
rcl_publisher_t publisher2;
std_msgs__msg__Float32MultiArray msg;
potmessage__msg__Potmsg potmsg;
buttonmessage__msg__Buttonmsg butmsg;

float data[8] = {3.14,1.0,2.0,3.0,4.0,5.0,6.0,7.0};

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
    RCSOFTCHECK(rcl_publish(&publisher2, &butmsg, NULL));
  }
}

float readJoint(int id) {
  // THIS IS JUST AVERAGE
  // TODO: implement moving average

  // Esta lendo e convertendo para graus
  double acc = 0;
  selecionarCanal(id);
  for (int i = 0; i < n_size; i++) {
    acc += analogRead(pinSaidaMux);
    ;
  }
  acc = acc / (n_size * 1.0);
  float degrees = acc;  //0.0699*acc-143.775;
  return degrees;
}

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}

void setup() {
  /*for (int i = 0; i < pot_size; i++){
    pinMode(POT_PINS[i], INPUT);
  }*/
  set_microros_transports();
  delay(300);

  allocator = rcl_get_default_allocator();

  //create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_arduino_node", "", &support));

  // create publisher
  RCCHECK(rclc_publisher_init_default(
    &publisher,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs ,msg, Float32MultiArray),
    "pot_topic"));
  RCCHECK(rclc_publisher_init_default(
    &publisher2,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(buttonmessage, msg, Buttonmsg),
    "button_topic"));

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

  potmsg.pot1 = 2.2;
  msg.data.data = data;
  msg.data.size = 8;
  msg.data.capacity = 8;

}

void loop() {
  delay(100);
  RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));

  for (int canal = 0; canal < 8; canal++) {
    selecionarCanal(canal);
    int valor = analogRead(pinSaidaMux);
    Serial.print("           ");
    Serial.print(canal);
    Serial.print(":");
    Serial.print(valor);
  }

}
