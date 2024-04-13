#include <Wire.h>

const int addrMux = 0x20;
const int pinSaidaMux = 34; 
const int pinS0 = 18;
const int pinS1 = 5; 
const int pinS2 = 17; 
const int pinS3 = 16; 

void setup() {
  Serial.begin(115200);
  Wire.begin();
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  pinMode(pinS3, OUTPUT);
}

void loop() {
  for (int canal = 0; canal < 8; canal++) {
    selecionarCanal(canal);
    int valor = analogRead(pinSaidaMux);
    Serial.print("Potenciômetro ");
    Serial.print(canal);
    Serial.print(": ");
    Serial.println(valor);
    delay(100);
  }
}

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
  digitalWrite(pinS3, (canal >> 3) & 0x01);
}