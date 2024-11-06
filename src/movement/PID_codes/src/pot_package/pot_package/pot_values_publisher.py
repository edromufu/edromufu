import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import serial
import time

class PotValuesPublisher(Node):
    def __init__(self, serial_port='/dev/ttyACM1', baud_rate=9600):
        super().__init__('pot_values_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'pot_values', 10)
        
        # Configuração da porta serial
        try:
            self.serial_connection = serial.Serial()
            self.serial_connection.port = serial_port
            self.serial_connection.baudrate = baud_rate
            self.serial_connection.open()

            time.sleep(2)  # Tempo para inicializar a conexão serial
            self.get_logger().info("Conexão serial estabelecida com sucesso.")
        except serial.SerialException as e:
            self.get_logger().error(f"Erro ao conectar com a porta serial: {e}")
            self.serial_connection = None
            return
        
        # Configuração do timer para publicar os dados a cada segundo
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        if self.serial_connection.in_waiting:
            try:
                # Lê a linha enviada pelo Arduino
                line = self.serial_connection.readline().decode('utf-8')
                self.get_logger().info(f"Linha recebida: {line}") 
                values = line.split(',')
                values.pop()
                values = [float(val) for val in values]
                
                

                # Verifica se o vetor tem 8 valores antes de publicar
                if len(values) == 8:
                    msg = Float64MultiArray()
                    msg.data = values
                    self.publisher_.publish(msg)
                    self.get_logger().info(f"Valores publicados: {msg.data}")
                else:
                    self.get_logger().warn(f"Vetor de tamanho inesperado: {len(values)}")

            except ValueError:
               self.get_logger().error("Erro ao converter os dados recebidos.")

def main(args=None):
    rclpy.init(args=args)
    node = PotValuesPublisher(serial_port='/dev/ttyACM1', baud_rate=9600)
    if node.serial_connection:
        rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
