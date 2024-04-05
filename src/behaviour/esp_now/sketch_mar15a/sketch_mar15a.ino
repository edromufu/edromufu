#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
const int potpin = 4;

esp_now_peer_info_t peerInfo;

typedef struct struct_message {
  uint16_t potValue;
} struct_message;
0x08, 0xD1, 0xF9, 0x27, 0xF9, 0x14
struct_message myData;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status);

void setup() {
  Serial.begin(115200);

  pinMode(potpin, INPUT);

  uint8_t broadcastAddress[] = {0x08, 0xD1, 0xF9, 0x27, 0xB6, 0x28}; // Replace with receiver's MAC address
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
}

void loop() {
  int potValue = analogRead(potpin);
  myData.potValue = potValue;
  int teste = 5;  // Definindo o valor de teste

  Serial.print("Potentiometer Value: ");
  Serial.println(potValue); // Imprimindo o valor do potenciômetro
  Serial.print("Teste Value: ");
  Serial.println(teste);  // Imprimindo o valor de teste
  

  delay(500);
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  esp_now_register_send_cb(OnDataSent);

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }

  esp_err_t result = esp_now_send(peerInfo.peer_addr, (uint8_t *)&myData, sizeof(myData));


  if (result != ESP_OK) {
    Serial.println("Error sending data via ESP-NOW");
  }
  WiFi.mode(WIFI_OFF);

}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}
