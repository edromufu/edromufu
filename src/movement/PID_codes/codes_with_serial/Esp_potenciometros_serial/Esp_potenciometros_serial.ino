#include <Arduino.h>


const int addMux = 0x20;
const int pinSaidaMux = 0;
const int pinS0 = 2;
const int pinS1 = 3;
const int pinS2 = 4;

int values[8];


void setup() {
  Serial.begin(9600);
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  
  analogSetPinAttenuation(33, ADC_0db);


void loop() {
  delay(300);
  for(int canal = 0; canal < 8; canal++){
    selecionarCanal(canal);
    int valor = analogRead(pinSaidaMux);
    Serial.print("              ");
    Serial.print(canal);
    Serial.print(":");
    Serial.print(valor);

  }
  Serial.println("   ");

}

void selecionarCanal(int canal){
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}
