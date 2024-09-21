#include <Wire.h>
#define SLAVE_ADDR 0x08  // Endereço I2C do Slave

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
float set_point[] = {0, 0, 0, 0, 0, 0, 0, 0};   //Ângulos a serem recebidos por ROS da cinemática inversa
int u_input[] =     {0, 0, 0, 0, 0, 0, 0, 0};   //Vetor de PWM a ser aplicado nos atuadores
int dt = 1000;                                  // tempo de amostragem em milisegundos


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



void setup() {
  Wire.begin();          // Configura o ESP32 como Master
  Serial.begin(115200);
  //for (int i = 0; i < pot_size; i++){initJoint(i);}  //Define todos os pinos a serem utilizados; Tá comentado pq tá usando um dos pinos que eu uso pra I2C
}

void loop() {
  
  //--------Receber valores Pot-------- 
  Wire.requestFrom(SLAVE_ADDR,8*sizeof(float));  // Solicita as 32 posições
  byte floatBytes[sizeof(float)*8]; //cria um vetor de 32 bytes
  Serial.println("Vetor de posições recebido: ");
  int index = 0;
  while (Wire.available()) {        
    floatBytes[index++] = Wire.read();   //recebe os 32 bytes
  }
  memcpy(atualPos, floatBytes, sizeof(float) * 8); //converte os 32 bytes de volta em 8 floats e aloca eles no vetor atualPos
  for (int i = 0; i < 8; i++) {
    Serial.println(atualPos[i]);   // Imprime cada float recebido
  }




  //--------Calculando Saídas dos PID's--------
  for (int i = 0; i < pot_size; i++){
    u_input[i] = calculatePID(i , set_point[i], atualPos[i]);
  }
  


  //--------Calculando Entrada do PWM--------
  writeActuator(0, u_input[1]-u_input[0]); //Ang 
  writeActuator(1, u_input[1]+u_input[0]);
  
  writeActuator(2, u_input[2]+u_input[3]);
  writeActuator(3, u_input[2]-u_input[3]);  
  writeActuator(4, u_input[4]+u_input[5]);
  writeActuator(5, u_input[4]-u_input[5]);
  writeActuator(6, u_input[6]+u_input[7]);
  writeActuator(7, u_input[6]-u_input[7]);
  


  delay(1000);  // Aguarda 1 segundo antes de solicitar novamente
}
