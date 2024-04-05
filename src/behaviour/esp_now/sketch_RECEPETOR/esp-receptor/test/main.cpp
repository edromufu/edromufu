#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>

esp_now_peer_info_t peerInfo;

typedef struct struct_message {
  uint16_t potValue;
} struct_message;

struct_message myData;

uint8_t pot_pins[] = {13, 12, 14, 27, 26, 25, 33, 32};
int npins = sizeof(pot_pins) / sizeof(pot_pins[0]);

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status);

void setup() {
    Serial.begin(115200);
    Serial.println("Início");
    
    for (int i = 0; i < npins; i++) {
        pinMode(pot_pins[i], OUTPUT);
    }

  uint8_t broadcastAddress[] = {0x24, 0x6F, 0x28, 0x52, 0x51, 0xA0}; // Replace with receiver's MAC address
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;


}

void loop() {
    // for (int i = 0 ; i < npins; i ++){
    //   Serial.print(i);
    //   Serial.print(": ");
    //   Serial.print(analogRead(pot_pins[i]));
    //   Serial.print("     ");
    // }
    Serial.print(0);
    Serial.print(": ");
    Serial.print(analogRead(pot_pins[0]));
    Serial.print("     ");    
    Serial.print(7);
    Serial.print(": ");
    Serial.print(analogRead(pot_pins[7]));
    Serial.print("     ");

    Serial.println(" ");
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
  
  delay(50);
    WiFi.mode(WIFI_OFF);
}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}