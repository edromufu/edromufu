#include "Arduino.h"
#include <Wire.h>

#define LED 2
#define tam 10//tamanho do vetor de media movel

const int MPU_addr = 0x68 ; // MPU-6050 I2C address
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;

float angles[tam]; //ultimas leituras do sensor
float medangle = 0;
int pos = 0; //posição do vetor na media movel
int range = 16384;//valor lido pelo sensor que corresponde a 180 graus

int minVal=265;
int maxVal=402;
 
double x;
double y;
double z;

int16_t mpu_read () {
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false) ;
  Wire.requestFrom(MPU_addr, 14, true); // request a total of 14 records
  AcX = Wire.read() << 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  AcY = Wire.read() << 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ = Wire.read() << 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp = Wire.read() << 8 | Wire.read(); // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  GyX = Wire.read() << 8 | Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY = Wire.read() << 8 | Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ = Wire.read() << 8 | Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
  /*Serial. print ( "Accelerometer values: \n" ) ;
  Serial. print ( "AcX: " ) ;
  Serial. print ( AcX ) ;
  Serial. print ( "\nAcY: " ) ;*/
  //Serial. println ( AcY ) ;
  /*
  Serial. print ( "\nAcZ: " ) ;
  Serial. print ( AcZ ) ;
  //Serial.print("\nTemperature: " );
  //Serial.print(Tmp);
  delay ( 1000 ) ;*/
  // Serial. print ( "\nGyroscope values:\t" ) ;
  Serial.print("yX: ");
  Serial.print(GyX);
  Serial.print(" \t GyY: ");
  Serial.print(GyY);
  Serial.print(" \t GyZ: ");
  Serial.print(GyZ);
  Serial.print("\n");
  return(AcY);
  
}

void setup() {
  // Set pin mode
  Serial.begin(9600);
  Wire.begin(23, 22, 100000);
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B); // Register PWR_MGMT_1
  Wire.write(0);    // set to zero (enables MPU-6050)
  Wire.endTransmission(true);
}

void loop() {
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);
  AcX=Wire.read()<<8|Wire.read();
  AcY=Wire.read()<<8|Wire.read();
  AcZ=Wire.read()<<8|Wire.read();
  int xAng = map(AcX,minVal,maxVal,-90,90);
  int yAng = map(AcY,minVal,maxVal,-90,90);
  int zAng = map(AcZ,minVal,maxVal,-90,90);
  
  x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI);
  y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI);
  z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);
  
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
  
}