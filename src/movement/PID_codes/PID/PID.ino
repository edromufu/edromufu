
//-------declaração de pinos-------
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
int dt = 1000; // tempo de amostragem em milisegundos

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
  pinMode(POT_PINS[id], INPUT);
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
  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }
  Serial.begin(9600);


}

void loop() {
  unsigned long now = millis();

  // [
  //   ((alfa, gama), (0, 1)),
  //   ((beta, epsilon), (2, 3))
  // ]



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
  for (int i = 0 ; i < pot_size ; i++){
    Serial.print(readJoint(i));
    writeActuator(3, -4000);
    Serial.print("\t");
  }
  Serial.println(" ");

  

  while (millis()-now<dt){
    // now = millis();
  }

}
