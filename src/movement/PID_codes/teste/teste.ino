// Definindo os pinos para controle do BTS7960
#define PWM_L 16     // Pino para controle PWM do lado baixo (DIR_L)
#define PWM_H 16     // Pino para controle PWM do lado alto (DIR_H)
#define DIR_L 17     // Pino para controle de direção (Low)
#define DIR_H 5     // Pino para controle de direção (High)

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
