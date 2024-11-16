const int ACTUATOR_IN_IMP_PINS[] = {26, 19, 2, 5, 32, 33, 13, 12}; //vetor de pino de avanço
const int ACTUATOR_IN_PAR_PINS[] = {22, 21, 4, 17, 16, 18, 27, 14};


void setup() {
   for(int i = 0; i < 8; i++){
    pinMode(ACTUATOR_IN_IMP_PINS[i], OUTPUT);
    pinMode(ACTUATOR_IN_PAR_PINS[i], OUTPUT);
   }
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 4; i++){
    digitalWrite(ACTUATOR_IN_IMP_PINS[i], HIGH);
    digitalWrite(ACTUATOR_IN_PAR_PINS[i], LOW);
   }

   for(int i = 4; i < 8; i++){
    digitalWrite(ACTUATOR_IN_IMP_PINS[i], LOW);
    digitalWrite(ACTUATOR_IN_PAR_PINS[i], HIGH);
   }
  delay(150);
   for(int i = 0; i < 4; i++){
    digitalWrite(ACTUATOR_IN_IMP_PINS[i], HIGH);
    digitalWrite(ACTUATOR_IN_PAR_PINS[i], LOW);
   }

   for(int i = 4; i < 8; i++){
    digitalWrite(ACTUATOR_IN_IMP_PINS[i], LOW);
    digitalWrite(ACTUATOR_IN_PAR_PINS[i], HIGH);
   }
}
