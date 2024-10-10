#include <Arduino.h>
#include <Wire.h>

const int addrMux = 0x20;
const int pinSaidaMux = 0; 
const int pinS0 = 2;
const int pinS1 = 3; 
const int pinS2 = 4; 

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}

void setup() {
  Serial.begin(9600);
  Serial.print("Começando...");
  Wire.begin();
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
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

