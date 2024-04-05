#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
const int potpin[] = {13,32};
const int numPorts = 2;
esp_now_peer_info_t peerInfo;

typedef struct struct_message {
  int potValue[2];
} struct_message;
struct_message myData;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status);

void setup() {
  Serial.begin(115200);
  analogSetPinAttenuation(13, ADC_0db);
  analogSetPinAttenuation(32, ADC_0db);

  for(int i = 0; i < numPorts; i++){
      pinMode(potpin[i], INPUT);
    }

  uint8_t broadcastAddress[] = {0x08, 0xD1, 0xF9, 0x27, 0xB6, 0x28}; // Replace with receiver's MAC address
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
}

void loop() {
  int potValue;
  Serial.print("Potentiometer Value: ");
  for(int i = 0; i < numPorts; i++){
    potValue = analogRead(potpin[i]);
    myData.potValue[i] = potValue;
    Serial.print(String(potValue)+" ");
    
  }
  Serial.println("ESP POT");
 

  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    abort();
    return;
  }
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    abort();
    return;
  }
  //esp_now_register_send_cb(OnDataSent);//Ve se os dados foram enviados

  esp_err_t result = esp_now_send(peerInfo.peer_addr, (uint8_t *)&myData, sizeof(myData));


  if (result != ESP_OK) {
    Serial.println("Error sending data via ESP-NOW");
  }
  WiFi.mode(WIFI_OFF);

}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}

