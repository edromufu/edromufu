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

void OnDataSent(const uint8_t *mac, const uint8_t *incomingData, int len);

void setup() {
  Serial.begin(115200);
  Wire.begin();
  pinMode(pinS0, OUTPUT);
  pinMode(pinS1, OUTPUT);
  pinMode(pinS2, OUTPUT);
  
  analogSetPinAttenuation(34, ADC_0db);


  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) return;
  
  uint8_t broadcastAddress[] = {0x08, 0xD1, 0xF9, 0x27, 0xF9, 0x14};
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}
uint16_t j = 0;
void loop() {
  for(int canal = 0; canal < 8; canal++){
    selecionarCanal(canal);
    int valor = analogRead(pinSaidaMux);
    Serial.print("           ");
    Serial.print(canal);
    Serial.print(":");
    Serial.print(valor);
    
    myData.potValue[canal] = j%4095;
  }
  j++;
  Serial.println(j);

  esp_err_t result = esp_now_send(peerInfo.peer_addr, (uint8_t *)&myData, sizeof(myData));


  if (result != ESP_OK) {
    Serial.println("Error sending data via ESP-NOW");
  }

}

void selecionarCanal(int canal){
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}