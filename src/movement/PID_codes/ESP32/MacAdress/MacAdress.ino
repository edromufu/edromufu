#include <WiFi.h>

<<<<<<< HEAD
void setup() {
  Serial.begin(115200);  // Inicializa a comunicação serial
  // Espera até a serial estar pronta
  while (!Serial) {
    ;
=======
void readMacAddress(){
  uint8_t baseMac[6];
  esp_err_t ret = esp_wifi_get_mac(WIFI_IF_STA, baseMac);
  if (ret == ESP_OK) {
    Serial.printf("%02x:%02x:%02x:%02x:%02x:%02x\n",
                  baseMac[0], baseMac[1], baseMac[2],
                  baseMac[3], baseMac[4], baseMac[5]);
  }
  else {
    Serial.println("Failed to read MAC address");
>>>>>>> refs/remotes/origin/PID
  }

  // Obter o endereço MAC
  String macAddress = WiFi.macAddress();

  // Exibe o endereço MAC no terminal serial
  Serial.print("MAC Address: ");
  Serial.println(macAddress);
}

void loop() {
  // O loop está vazio, pois só precisamos imprimir o endereço MAC uma vez
}
