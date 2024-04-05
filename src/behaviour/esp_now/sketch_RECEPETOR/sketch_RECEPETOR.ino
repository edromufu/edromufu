
#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>

esp_now_peer_info_t peerInfo;
int potPrint[2];
int numPorts=2;
typedef struct struct_message {
  int potValue[2];
} struct_message;
struct_message myData;

void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len);

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) return;

  esp_now_register_recv_cb(OnDataRecv);

  uint8_t broadcastAddress[] = {0xB4, 0xE6, 0x2D, 0xCF, 0x35, 0x81}; 
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  Serial.print("Potentiometer Value: ");
  for (int i = 0; i < numPorts; i++){
    potPrint[i] = myData.potValue[i];
    Serial.print(String(potPrint[i]) + " ");
    }
  Serial.println("Receiver");
  
}

void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));
}
