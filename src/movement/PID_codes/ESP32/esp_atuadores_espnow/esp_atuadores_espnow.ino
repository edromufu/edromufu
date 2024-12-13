
#include <Arduino.h>
#include <esp_now.h>
#include <micro_ros_arduino.h>
#include <WiFi.h>
// MicroROS Libraries
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/float32_multi_array.h>

// MicroROS Variaveis
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;
//rcl_publisher_t publisher;
rcl_publisher_t publisher2;
rcl_subscription_t subscriber;

std_msgs__msg__Float32MultiArray feedbackMsg;
//std_msgs__msg__Float32MultiArray msg;
// ------------------------------------

esp_now_peer_info_t peerInfo;

int potPrint[8];
int numPorts=8;


//======================================

//============== MicroROS ==============
#define RCCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) { abort(); } \
  }
#define RCSOFTCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) {abort();} \
  }
void error_loop() {
  Serial.println("ERROR LOOP");
}
void timer_callback(rcl_timer_t* timer, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer != NULL) {
    //RCSOFTCHECK(rcl_publish(&publisher, &msg, NULL));
 }
 }
//======================================

// ================ PID ================
//------- Pinos -------
//--------constantes Graus--------
float erro[8];
const int pot_size = 8;

//--------constantes Drivers-------- ****TEM QUE PEGAR TUDO DO DIAGRAMA DA ELÉTRICA!!!!!!!****
//const int ACTUATOR_EN_PINS[] =     {x, 33, 27, 13, 15, 19, 17, 2}; //vetor de PWM
//const int ACTUATOR_IN_IMP_PINS[] = {13, 33, 25, 14, 23, 15, 18, 16}; //vetor de pino de avanço
//const int ACTUATOR_IN_PAR_PINS[] = {27, 32, 26, 12, 22, 21, 5, 4}; //vetor de pino de recuo
const int ACTUATOR_RPWM[] = {13, 12, 14, 27, 26, 25, 33, 32}; // Pinos de Recuo quando HIGH
const int ACTUATOR_LPWM[] = {17, 5, 15, 2, 0, 4, 16, 18}; // Pinos de Avanço quando HIGH

//--------constantes PID--------

const float Kp[]  =  {100, 100, 100, 100, 100, 100, 100, 100};
const float Ki[]  =  {0, 0, 0, 0, 0, 0, 0, 0};
const float Kd[]  =  {0, 0, 0, 0, 0, 0, 0, 0};
float lastError[] =  {0, 0, 0, 0, 0, 0, 0, 0};
float accError[]  =  {0, 0, 0, 0, 0, 0, 0, 0};
float data[]      =  {0, 0, 0, 0, 0, 0, 0, 0};   //Ângulos a serem recebidos por ROS da cinemática inversa
float u_input[]   =  {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de PWM a ser aplicado nos atuadores
float feedback[]  =  {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de feedback
int   dt = 1000;   
float feedbackData[8];                               // tempo de amostragem em milisegundos




// --------- Funçoes ---------

void initJoint(){
  for (int i = 0; i < pot_size; i++){
    //pinMode(ACTUATOR_EN_PINS[i], OUTPUT);
    pinMode(ACTUATOR_RPWM[i], OUTPUT);
    pinMode(ACTUATOR_LPWM[i], OUTPUT);
  }
}


float calculatePID(int id, float erro){

  float derro = 1000*(erro - lastError[id])/dt;
  
  accError[id]+= erro*dt/1000;

  int u = Kp[id]*erro +Ki[id]*accError[id]+ Kd[id]*derro;
  return u;
}


void writeActuator (int id, int signal){
  // Pega o valor de u fornecido pelo PID e transforma em comandos para os drivers
  // id: id da junta
  // signal: valor de -4095 4095 para escrever na junta
  //int newSignal = constrain(signal, -255, 255);
  feedback[id]=0.0; // era signal
  if (signal < -5){
    digitalWrite(ACTUATOR_RPWM[id], LOW); //Quando o erro é negativo o atuador linear avança
    digitalWrite(ACTUATOR_LPWM[id], HIGH);
    //analogWrite(ACTUATOR_EN_PINS[id], newSignal);
    feedback[id]=-1.0;
  }
  else if (signal > 5){
    digitalWrite(ACTUATOR_RPWM[id], HIGH); //Quando o erro é positivo o atuador linear retrai
    digitalWrite(ACTUATOR_LPWM[id], LOW);
        feedback[id]=1.0;
    //analogWrite(ACTUATOR_EN_PINS[id], -newSignal);
  }else if(signal <= 5 && signal >= -5){
    
    digitalWrite(ACTUATOR_RPWM[id], LOW);
    digitalWrite(ACTUATOR_LPWM[id], LOW);
    feedback[id]=5.0;
  }
}

void setup() {


  initJoint();
  



  set_microros_transports();
  delay(300);

  allocator = rcl_get_default_allocator();

  //create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_pot_node", "", &support));

  // create publisher
  //RCCHECK(rclc_publisher_init_default(&publisher,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs ,msg, Float32MultiArray),"pot_topic"));
  RCCHECK(rclc_publisher_init_default(&publisher2,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32MultiArray),"pot_feedback_topic"));
  RCCHECK(rclc_subscription_init_default(&subscriber,&node,ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32MultiArray),"pot_values"));

  // create timer,
  const unsigned int timer_timeout = 100;
  RCCHECK(rclc_timer_init_default(
    &timer,
    &support,
    RCL_MS_TO_NS(timer_timeout),
    timer_callback));


  // create executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
  RCCHECK(rclc_executor_add_timer(&executor, &timer));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &feedbackMsg, &subscription_callback, ON_NEW_DATA));

  feedbackMsg.data.data = (float *) malloc(8 * sizeof(float));
  feedbackMsg.data.size = 8;
  feedbackMsg.data.capacity = 8;
}

void loop() {
  
  RCSOFTCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));

}

void subscription_callback(const void * msgin)
{  
  const std_msgs__msg__Float32MultiArray * feedbackSub = (const std_msgs__msg__Float32MultiArray *)msgin;

  for(int i = 0; i < 8; i++){
    //--------Recebendo o erro--------
    erro[i] = feedbackSub->data.data[i];

    //--------Calculando Saídas dos PID's--------
  }

  CalculatePWM();
  feedbackMsg.data.data = feedback;

  RCSOFTCHECK(rcl_publish(&publisher2, &feedbackMsg, NULL));

}

void CalculatePWM(){

  //--------Calculando Entrada do PWM--------
  writeActuator(0, erro[0]); //(erro[0]-erro[1])
  //writeActuator(1, erro[1]);//(-erro[0]-erro[1])
  //writeActuator(2, -erro[2]); //(erro[0]-erro[1])
  //writeActuator(3, -erro[2]);//(-erro[0]-erro[1])
  //writeActuator(4, erro[5]); //(erro[0]-erro[1])
  //writeActuator(5, erro[5]);//(-erro[0]-erro[1])

  //writeActuator(6, erro[6]); //(erro[0]-erro[1])
  writeActuator(7, erro[7]);//(-erro[0]-erro[1])
/*
  if(abs(erro[0])<5){
    writeActuator(0, erro[1]); //(erro[0]-erro[1])
    writeActuator(1, erro[1]);//(-erro[0]-erro[1])
  }

  writeActuator(2, erro[3]);//(erro[2]+erro[3])
  writeActuator(3, -erro[3]);//(erro[2]-erro[3])

  if(abs(erro[3])<5){
    writeActuator(2, -erro[2]);//(erro[2]+erro[3])
    writeActuator(3, -erro[2]);//(erro[2]-erro[3])
  }


  writeActuator(4, erro[5] );//(erro[5] + erro[4])
  writeActuator(5, erro[5] );//(erro[5] -erro[4])
  writeActuator(4, + erro[4]);//(erro[5] + erro[4])
  writeActuator(5, -erro[4]);

  writeActuator(6, -erro[6]);
  writeActuator(7, -erro[6]);
  writeActuator(6, -erro[7]);
  writeActuator(7, +erro[7]);*/

}
