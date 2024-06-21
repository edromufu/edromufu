
const int POT_PINS[] = {34, 35, 32, 33}; // vetor de portas de potenciômetros
const int ACTUATOR_EN_PINS[] =  {23,  5, 27,  4}; //vetor de PWM
const int ACTUATOR_INA_PINS[] = {22, 19, 26, 15}; //vetor de pino de avanço
const int ACTUATOR_INB_PINS[] = {21, 18, 25,  2}; //vetor de pino de recuo
const int pot_size = 4; //número de juntas
int pot_values[pot_size]; // valores lidos na junta
const int n_size = 15; // quantidade de média móvel

int dt = 100; // tempo de amostragem em milisegundos

float readJoint(int id){
  // THIS IS JUST AVERAGE
  // TODO: implement moving average
  double acc = 0;
  for (int i = 0; i<n_size; i++){
    acc+= analogRead(POT_PINS[id]);
  }
  acc = acc/n_size;
  float degrees = 0.0699*acc-143.775;
  return degrees;
}

void writeActuator (int id, int signal){
  // id: id da junta
  // signal: valor de -10000 10000 para escrever na junta
  if (signal >= 0){
    digitalWrite(ACTUATOR_INA_PINS[id], HIGH);
    digitalWrite(ACTUATOR_INB_PINS[id], LOW);
    analogWrite(ACTUATOR_EN_PINS[id], signal);
  }
  if (signal < 0){
    digitalWrite(ACTUATOR_INA_PINS[id], LOW);
    digitalWrite(ACTUATOR_INB_PINS[id], HIGH);
    analogWrite(ACTUATOR_EN_PINS[id], -signal);
  }
}

void initJoint(int id){
  pinMode(POT_PINS[id], INPUT);
  pinMode(ACTUATOR_EN_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INA_PINS[id], OUTPUT);
  pinMode(ACTUATOR_INB_PINS[id], OUTPUT);
}




void setup() {
  for (int i = 0; i < pot_size; i++){
    initJoint(i);
  }
  Serial.begin(9600);


}

void loop() {

  for (int j = 0; j<pot_size; j++){
    float value = readJoint(j);
    Serial.print(value);
    Serial.print("\t");
  }

  Serial.println("\t");
  

  // val2 = analogRead(P2);
  // val3 = analogRead(P3);
  // val4 = analogRead(P4);
  // Serial.print(val1);
  // Serial.print("\t");
  // Serial.print(val2);
  // Serial.print("\t");
  // Serial.print(val3);
  // Serial.print("\t");
  // Serial.print(rintln("\t");
  // Serial.println("\t");
  delay(50);

  // put your main code here, to run repeatedly:

}
