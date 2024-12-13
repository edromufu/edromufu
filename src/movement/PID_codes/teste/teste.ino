// Definindo os pinos para controle do BTS7960
#define PWM_L 2  // 13, 12, 14, 27,26,25, 33, 32,  // Pino para controle PWM do lado baixo (DIR_L)
#define PWM_H 2      //  17, 5 , 15, 2, 0, 4, 16, 18   Pino para controle PWM do lado alto (DIR_H)
#define DIR_L 18     // Pino para controle de direção (Low) L_PWM LOW -> Recuo
#define DIR_H 5    // Pino para controle de direção (High) R_PWM HIGH -> Recuo

// Variáveis de controle do PWM
int motorSpeed = 255;  // Velocidade do motor (0 a 255)
int motorDirection = 1; // 1 = sentido horário, -1 = sentido anti-horário

void setup() {
  // Inicializando os pinos como saída
  pinMode(PWM_L, OUTPUT);
  pinMode(PWM_H, OUTPUT);
  pinMode(DIR_L, OUTPUT);
  pinMode(DIR_H, OUTPUT);


  // Definindo a direção inicial
  digitalWrite(DIR_L, LOW);  // Inicialmente, a direção é para frente
  digitalWrite(DIR_H, HIGH);
  analogWrite(PWM_H, motorSpeed);
}

void loop() {
  // Verificando a direção
  if (motorDirection == 1) {
    // Direção para frente (sentido horário)
    digitalWrite(DIR_L, LOW);
    digitalWrite(DIR_H, HIGH);
  } else if (motorDirection == -1) {
    // Direção para trás (sentido anti-horário)
    digitalWrite(DIR_L, HIGH);
    digitalWrite(DIR_H, LOW);
  }

  delay(1000);  // Espera 1 segundo

  // Alternando a direção após 1 segundo
  motorDirection *= -1; // Muda a direção
  delay(1000); // Espera mais 1 segundo
}
