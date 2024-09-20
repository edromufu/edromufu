/*#include <Wire.h>


//-------declaração de pinos-------
#define LED_PIN 13

//-------declaração do endereço do slave-------
#define SLAVE_ADDR 0x08 

const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; //vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; //vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; //vetor de pino de recuo
const int pot_size = 4; //número de juntas


//--------constantes PID--------
const float Kp[] = {10, 10, 10, 10};
const float Ki[] = {0, 0, 0, 0};
const float Kd[] = {0, 0, 0, 0};
float lastError[] = {0, 0, 0, 0};
float accError[] = {0, 0, 0, 0};
float angles[] = {0, 0, 0, 0, 0, 0, 0, 0};
int dt = 1000; // tempo de amostragem em milisegundos





void readJoint(){
  Wire.requestFrom(SLAVE_ADDR,4);
  Serial.print("Vetor de posições recebido: ");
  while (Wire.available()) {        // Enquanto houver dados disponíveis
    int posicao = Wire.read();      // Lê um byte de dados
    Serial.print(posicao);
    Serial.print(" ");
  }
  Serial.println("");
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

  Wire.begin();
  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }
  Serial.begin(19200);


}

void loop() {
  unsigned long now = millis();

  // [
  //   ((alfa, gama), (0, 1)),
  //   ((beta, epsilon), (2, 3))
  // ]


  // Serial.println(potmsg.pot1);
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
  readJoint();
  delay(500);
  }*/


#include <Wire.h>
#define SLAVE_ADDR 0x08  // Endereço I2C do Slave

//--------constantes Graus--------
float atualPos[8];
const int pot_size = 8;


//--------constantes Drivers-------- ****TEM QUE PEGAR TUDO DO DIAGRAMA DA ELÉTRICA!!!!!!!****
const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; //vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; //vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; //vetor de pino de recuo

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


void writeActuator (int id, int signal){
  // Pega o valor de u fornecido pelo PID e transforma em comandos para os drivers
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
  writeActuator(0, u_input[0]+u_input[1]);
  writeActuator(1, u_input[0]-u_input[1]);
  writeActuator(2, u_input[2]+u_input[3]);
  writeActuator(3, u_input[2]-u_input[3]);  
  writeActuator(4, u_input[4]+u_input[5]);
  writeActuator(5, u_input[4]-u_input[5]);
  writeActuator(6, u_input[6]+u_input[7]);
  writeActuator(7, u_input[6]-u_input[7]);
  


  delay(1000);  // Aguarda 1 segundo antes de solicitar novamente
}