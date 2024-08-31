#include <micro_ros_arduino.h>

#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>

#include <potmessage/msg/potmsg.h>

rcl_subscription_t subscriber;
rclc_executor_t executor;
potmessage__msg__Potmsg potmsg;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;


//-------declaração de pinos-------
#define LED_PIN 13
const int POT_PINS[] = {34, 35, 32, 33}; // vetor de portas de potenciômetros
const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; //vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; //vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; //vetor de pino de recuo
const int pot_size = 4; //número de juntas


//----------variáveis----------
int pot_values[pot_size]; // valores lidos na junta
const int n_size = 15; // quantidade de média móvel

//--------constantes PID--------
const float Kp[] = {10, 10, 10, 10};
const float Ki[] = {0, 0, 0, 0};
const float Kd[] = {0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0};
float accError[] = {0, 0, 0, 0};
float angles[] = {0, 0, 0, 0, 0, 0, 0, 0};
int dt = 1000; // tempo de amostragem em milisegundos


//-------ros2----------
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

void error_loop(){
  while(1){
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    delay(100);
  }
}

void subscription_callback(const void * msgin){  
  const potmessage__msg__Potmsg * msg = (const potmessage__msg__Potmsg *)msgin;
}

// aqui fica o subscriber
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


void setup() {
  set_microros_transports();
  delay(100);
  allocator = rcl_get_default_allocator();
  
  //create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "esp_actuators", "", &support));

  // create subscriber
  RCCHECK(rclc_subscription_init_default(
    &subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(potmessage, msg, Potmsg),
    "esp_actuators_subscriber"));

  // create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &potmsg, &subscription_callback, ON_NEW_DATA));


  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }
  Serial.begin(19200);


}

void loop() {
  unsigned long now = millis();
  RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));

  // [
  //   ((alfa, gama), (0, 1)),
  //   ((beta, epsilon), (2, 3))
  // ]


  // Serial.println(potmsg.pot1);
  Serial.println(millis());
  // float yalfa = readJoint(1);
  // int ualfa = calculatePID(1, 10, yalfa);

  // float ygama = readJoint(0);
  // int ugama = calculatePID(0, 5, ygama);


  // writeActuator(0, ualfa + yalfa);
  // writeActuator(1, ugama - ygama);




  // float ybeta = readJoint(2);
  // int ubeta = calculatePID(1, 10, ybeta);

  // float yepsilon = readJoint(3);
  // int uepsilon = calculatePID(0, 5, yepsilon);


  // writeActuator(2, ubeta + ybeta);
  // writeActuator(3, uepsilon - yepsilon);
  // for (int i = 0 ; i < pot_size ; i++){
  //   Serial.print(readJoint(i));
  //   writeActuator(3, -4000);
  //   Serial.print("\t");
  // }
  // Serial.println(" ");

  

  while (millis()-now<dt){
    // now = millis();
  }

}
