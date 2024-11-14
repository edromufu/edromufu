import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import serial
import time

class PotValuesPublisher(Node):
    def __init__(self, serial_port='/dev/ttyACM0', baud_rate=9600):
        super().__init__('pot_values_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'pot_values', 1)
        self.subscriber_ = self.create_subscription(Float32MultiArray,'pot_py_topic',self.listener,1)
        self.pagePoses=[ 0,0,0,0,0,0,0,0]
        self.vetor_reordenado =[ 0,0,0,0,0,0,0,0]
        self.errors =[ 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.posicoesPot=[6,5,7,4,3,0,1,2]
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
            serial_port = '/dev/ttyACM1'
            self.serial_connection = serial.Serial()
            self.serial_connection.port = serial_port
            self.serial_connection.baudrate = baud_rate
            self.serial_connection.open()
            self.serial_connection = None
            return
        
        # Configuração do timer para publicar os dados a cada segundo
        self.timer = self.create_timer(0.1, self.timer_callback)

    def listener(self, msg):
        self.pagePoses = msg.data

       

       

        

    def timer_callback(self):
        if self.serial_connection.in_waiting:
            try:
                # Lê a linha enviada pelo Arduino
                line = self.serial_connection.readline().decode('utf-8')
                
                values = line.split(',')
                values.pop()
                values = [float(val) for val in values]
                self.vetor_reordenado = [0] * len(values)
                for i, pos in enumerate(self.posicoesPot):
                    try:
                        self.vetor_reordenado[pos] = values[i]
                    except:
                        pass
                for i in (range(8) if len(self.vetor_reordenado)>=8 else range(len(self.vetor_reordenado))):
                    self.errors[i] = self.vetor_reordenado[i] - self.pagePoses[i]
                #if(sum(self.errors) <= 50):
                #    self.pagePoses.pop(1)
                

                # Verifica se o vetor tem 8 valores antes de publicar
                self.get_logger().info(f"Linha recebida: {self.vetor_reordenado}") 
                if len(values) == 8:
                    msg = Float32MultiArray()
                    msg.data = self.errors
                    self.publisher_.publish(msg)
                    self.get_logger().info(f"Valores publicados: {msg.data}")
                else:
                    self.get_logger().warn(f"Vetor de tamanho inesperado: {len(values)}")

            except ValueError:
               self.get_logger().error("Erro ao converter os dados recebidos.")

def main(args=None):
    rclpy.init(args=args)
    node = PotValuesPublisher()
    if node.serial_connection:
        rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
