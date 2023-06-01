#!/usr/bin/env python3
import dynamixel_sdk as dxl
import time

# Parâmetros da comunicação com os motores Dynamixel
BAUDRATE = 1000000  # Velocidade de comunicação
DEVICENAME = '/dev/ttyUSB0'  # Porta serial a ser utilizada

# IDs dos motores
MX_ID = 0
AX_ID = 4

# Endereços dos registradores
MX_LED_ADDR = 65  # Endereço do registrador de controle do LED para o AX-12
AX_LED_ADDR = 25  # Endereço do registrador de controle do LED para o AX-12

# Inicialização da comunicação com os motores
port_handler = dxl.PortHandler(DEVICENAME)
AX_packet_handler = dxl.PacketHandler(1.0) 
MX_packet_handler = dxl.PacketHandler(2.0)

# Abrir a porta serial
if port_handler.openPort():
    print("Porta serial aberta com sucesso")
else:
    print("Não foi possível abrir a porta serial")
    exit(1)

# Configurar a velocidade de comunicação
if port_handler.setBaudRate(BAUDRATE):
    print("Velocidade de comunicação configurada com sucesso")
else:
    print("Não foi possível configurar a velocidade de comunicação")
    exit(1)

# Função para acender o LED de um motor
def ligar_led(id_motor, packet_handler, addr):
    packet_handler.write1ByteTxRx(port_handler, id_motor, addr, 1)

# Função para apagar o LED de um motor
def desligar_led(id_motor, packet_handler, addr):
    packet_handler.write1ByteTxRx(port_handler, id_motor, addr, 0)

while True: 
    # Acender o LED do motor MX-106
    ligar_led(MX_ID, MX_packet_handler, MX_LED_ADDR)

    # Acender o LED do motor AX-12
    ligar_led(AX_ID, AX_packet_handler, AX_LED_ADDR)

    # Aguardar alguns segundos

    time.sleep(0.5)

    # Apagar o LED do motor MX-106
    desligar_led(MX_ID, MX_packet_handler, MX_LED_ADDR)

    # Apagar o LED do motor AX-12
    desligar_led(AX_ID, AX_packet_handler, AX_LED_ADDR)

    time.sleep(0.5)

# Fechar a porta serial
port_handler.closePort()
