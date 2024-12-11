#include <Arduino.h>


const int addMux = 0x20;
const int pinSaidaMux = 35;
const int pinS0 = 21;
const int pinS1 = 22;
const int pinS2 = 23;
float valor = 0.0;

int values[8];


void setup() {
  Serial.begin(9600);
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  pinMode(pinSaidaMux,INPUT);

  //analogSetPinAttenuation(3, ADC_0db);
}

void loop() {
  delay(100);
  
  for (int canal = 0; canal < 8; canal++) {
    selecionarCanal(canal);
    for (int j =0; j < 100; j++){
    valor += (analogRead(pinSaidaMux) - 2048) * 0.06491;
    }
    valor = valor/100;
    Serial.print(valor);
    Serial.print(",");
  }
  Serial.println("   ");
  delay(10);
}

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}
