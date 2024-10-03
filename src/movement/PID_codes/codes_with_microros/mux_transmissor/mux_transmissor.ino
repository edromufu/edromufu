#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
#include <Wire.h>

const int addMux = 0x20;
const int pinSaidaMux = 34;
const int pinS0 = 14;
const int pinS1 = 27;
const int pinS2 = 26;
esp_now_peer_info_t peerInfo;

int values[8];

typedef struct struct_message {
  uint16_t potValue[8];
} struct_message;
struct_message myData;

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  analogSetPinAttenuation(34, ADC_0db);

  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) return;

  uint8_t broadcastAddress[] = {0xD0,0xEF,0x76,0x34,0x78,0xAC};//Coloca o endereço MAC do esp com o ROS
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  for (int canal = 0; canal < 8; canal++) {
    selecionarCanal(canal);
    int valor = analogRead(pinSaidaMux);
    myData.potValue[canal] = valor;
  }

  esp_err_t result = esp_now_send(peerInfo.peer_addr, (uint8_t *)&myData, sizeof(myData));
  if (result != ESP_OK) {
    Serial.println("Error sending data via ESP-NOW");
  }
  delay(100);

//Talvez adiciona delay caso esteja dando algum tipo de gargalo
}
