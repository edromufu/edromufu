
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

100l_publish(&publisher, &msg, NULL));

  }
}
//======================================

// ================ PID ================
//------- Pinos -------
//--------constantes Graus--------
float erro[8];
const int pot_size = 8;


//--------constantes Drivers-------- ****TEM QUE PEGAR TUDO DO DIAGRAMA DA ELÉTRICA!!!!!!!****
const int ACTUATOR_EN_PINS[] =     {34, 33, 27, 13, 15, 19, 17, 2}; //vetor de PWM
const int ACTUATOR_IN_IMP_PINS[] = {36, 35, 25, 14, 23, 3, 18, 16}; //vetor de pino de avanço
const int ACTUATOR_IN_PAR_PINS[] = {39, 32, 26, 12, 22, 21, 5, 4}; //vetor de pino de recuo

//--------constantes PID--------

const float Kp[] =  {10, 10, 10, 10, 10, 10, 10, 10};
const float Ki[] =  {0, 0, 0, 0, 0, 0, 0, 0};
const float Kd[] =  {0, 0, 0, 0, 0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0, 0, 0, 0, 0};
float accError[] =  {0, 0, 0, 0, 0, 0, 0, 0};
float data[] =      {0, 0, 0, 0, 0, 0, 0, 0};   //Ângulos a serem recebidos por ROS da cinemática inversa
float u_input[] =     {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de PWM a ser aplicado nos atuadores
float feedback[] =     {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de feedback
int dt = 1000;                                  // tempo de amostragem em milisegundos




// --------- Funçoes ---------

void initJoint(int id){
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_IMP_PINS[id], OUTPUT);
  pinMode(ACTUATOR_IN_PAR_PINS[id], OUTPUT);
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
  int newSignal = constrain(signal, -4095.0, 4095.0);
  feedback[id]=newSignal;
  if (signal >= 0){
    digitalWrite(ACTUATOR_IN_IMP_PINS[id], LOW);
    digitalWrite(ACTUATOR_IN_PAR_PINS[id], HIGH);
    analogWrite(ACTUATOR_EN_PINS[id], newSignal);
  }
  if (signal < 0){
    digitalWrite(ACTUATOR_IN_IMP_PINS[id], HIGH);
    digitalWrite(ACTUATOR_IN_PAR_PINS[id], LOW);
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

  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }


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
    u_input[i] = calculatePID(i, erro[i]);
  }

  CalculatePWM();
  feedbackMsg.data.data = feedback;

  RCSOFTCHECK(rcl_publish(&publisher2, &feedbackMsg, NULL));

}

void CalculatePWM(){

  //--------Calculando Entrada do PWM--------
  writeActuator(0, u_input[1]+u_input[0]); 
  writeActuator(1, u_input[1]-u_input[0]);
  
  writeActuator(2, u_input[2]+u_input[3]);
  writeActuator(3, u_input[2]-u_input[3]);
  
  writeActuator(4, u_input[5]+u_input[4]);
  writeActuator(5, u_input[5]-u_input[4]);
  
  writeActuator(6, u_input[6]+u_input[7]);
  writeActuator(7, u_input[6]-u_input[7]);
}
