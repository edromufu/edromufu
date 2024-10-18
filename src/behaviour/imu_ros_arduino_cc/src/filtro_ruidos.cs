#include <SPI.h>
#include <Wire.h>
#define MPU 0x68  // Endereço I2C do MPU-6050

double AcX, AcY, AcZ;
double AcX_m, AcY_m, AcZ_m; // Variáveis para valores em m/s²
double GyX, GyY, GyZ;
double rollC = 0.0, rollAccel;
double X = 0.98; // Constante de suavização
unsigned long previousTime = 0, currentTime, printTime = 0, initTime = 0;
double elapsedTime;
bool mpuInitialized = false;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  init_MPU(); // Inicialização do MPU6050
  previousTime = millis(); // Inicializa o tempo anterior
  printTime = millis(); // Inicializa o tempo para impressão dos dados
  mpuInitialized = true;
}

void loop() {
  currentTime = millis(); // Atualiza o tempo atual

  elapsedTime = (currentTime - previousTime) / 1000.0; // Calcula o tempo decorrido em segundos
  previousTime = currentTime; // Atualiza o tempo anterior

  // Inicia a comunicação com o MPU-6050
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  // Começa no registro 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 14, true); // Solicita um total de 14 registros

  // Leitura dos dados do acelerômetro
  AcX = Wire.read() << 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  AcY = Wire.read() << 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ = Wire.read() << 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

  Wire.read(); Wire.read(); // Ignora os registros de temperatura (0x41 & 0x42)

  // Leitura dos dados do giroscópio
  GyX = Wire.read() << 8 | Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY = Wire.read() << 8 | Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ = Wire.read() << 8 | Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  // Converte os valores brutos do acelerômetro para m/s²
  AcX_m = (AcX / 16384.0) * 9.81;
  AcY_m = (AcY / 16384.0) * 9.81;
  AcZ_m = (AcZ / 16384.0) * 9.81;

  // Cálculo do valor de roll baseado no acelerômetro
  rollAccel = atan2(AcY, AcZ) * 180 / 3.14;

  // Converte os valores brutos do giroscópio para graus por segundo
  GyX = GyX / 131.0;
  GyY = GyY/ 131.0;
  GyZ = GyZ/ 131.0;

  // Cálculo do novo valor de Roll, rollC usando o filtro complementar
  rollC = (1 - X) * rollAccel + X * (rollC + GyX * elapsedTime);

  
  if (currentTime - printTime >= 500) { /
    Serial.print("RollC: "); Serial.print(rollC);
    Serial.print(" | AcX: "); Serial.print(AcX_m); 
    Serial.print(" | AcY: "); Serial.print(AcY_m); 
    Serial.print(" | AcZ: "); Serial.print(AcZ_m); 
    Serial.print(" | GyX: "); Serial.print(GyX);
    Serial.print(" | GyY: "); Serial.print(GyY);
    Serial.print(" | GyZ: "); Serial.print(GyZ);
    Serial.print("\n");
    printTime = currentTime; 
  }
}

void init_MPU() {
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);  
  Wire.write(0);     
  Wire.endTransmission(true);
}