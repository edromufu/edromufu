
const int POT_PINS[] = {34, 35, 32, 33};
const int pot_size = 4;
int pot_values[pot_size];
int current_pos = 0;
const int n_size = 15;
int MAT_POT[pot_size][n_size];
int POT_INDEX = 0;


void setup() {
  for (int i = 0; i < pot_size; i++){
    pinMode(POT_PINS[i], INPUT);
  }
  Serial.begin(9600);


}

void loop() {

  for (int i = 0; i < pot_size; i++){
    MAT_POT[i][POT_INDEX] = analogRead(POT_PINS[i]);
    
    int acc = 0;
    for(int j = 0; j < n_size; j++) {
      acc += MAT_POT[i][j];
    }
    pot_values[i] = acc / n_size;
    int printavel = 0.0699*pot_values[i]-143.775;
    Serial.print(printavel);
    Serial.print("\t");
  }

  POT_INDEX = (POT_INDEX + 1) % n_size;

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
