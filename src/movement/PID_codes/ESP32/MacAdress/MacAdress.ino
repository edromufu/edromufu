#include <WiFi.h>

void setup() {
  Serial.begin(115200);  // Inicializa a comunicação serial
  // Espera até a serial estar pronta
  while (!Serial) {
    ;
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
