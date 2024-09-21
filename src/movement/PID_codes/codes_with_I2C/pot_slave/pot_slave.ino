#include <Wire.h>

#define SDA_PIN 20
#define SCL_PIN 21

//---------Pot----------------
const int pot_size = 8;    // Mudar pra 8
const int n_size = 15;     // quantidade de média móvel
float ang_values[pot_size];  // valores lidos na junta
//----------------------------


//---------Mux----------------
const int addMux = 0x20;
const int pinSaidaMux = 0;
const int pinS0 = 2;
const int pinS1 = 3;
const int pinS2 = 4;
//----------------------------

void selecionarCanal(int canal) {
  digitalWrite(pinS0, canal & 0x01);
  digitalWrite(pinS1, (canal >> 1) & 0x01);
  digitalWrite(pinS2, (canal >> 2) & 0x01);
}

void setup() {
  Wire.begin(0x08, SDA_PIN, SCL_PIN);                 // Configura o ESP32 como Slave com endereço 0x08
  Wire.onRequest(requestEvent);     // Configura a função de callback para envio de dados
  Serial.begin(115200);
  pinMode(pinSaidaMux, INPUT);
}

float readJoint() {
  // TODO: implement moving average

  double acc = 0;
  for (int i = 0; i < n_size; i++) {acc += analogRead(pinSaidaMux);}
  acc = acc / (n_size * 1.0);
  float degrees = 0.0699*acc-143.775;  //0.0699*acc-143.775; Tem que fazer a linearização!!!!!
  return degrees;
}

void loop() { delay(100);}// Não há necessidade de ações no loop, o Slave só responde a solicitações


// Função chamada quando o  solicita dados
void requestEvent() {
  for (int i = 0; i < pot_size; i++) {
    selecionarCanal(i);
    ang_values[i] = readJoint();
    }

  byte* bytePtr = (byte*) &ang_values;
  for (int j=0; j<sizeof(ang_values);j++){ 
    Wire.write(bytePtr[j]); // Envia os elementos frutos da readJoint, que é 
  }  

  Serial.println("Dados enviados!");
  for (int i=0; i<8; i++){
  Serial.println(ang_values[i]);
  }

}
