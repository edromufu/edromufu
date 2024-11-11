import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Float32  # Usado para publicar o vetor de movimento (x, y)
####from sensor_msgs.msg import Imu  # Usado para publicar os dados do IMU (Inertial Measurement Unit)
from pynput import keyboard  # Para capturar eventos de teclado
from ParticleFilter import ParticleFilter as pf

#! Converter ou alterar ângulos o imu
# W/S Manda +-delta x
# A/D Manda -+ delta y
# Q/E Altera +- delta phi
# Z/Xq Altera +- delta neckUZ

class TestPublisher(Node):

    def __init__(self):
        super().__init__('test_publisher')

        # Criando os publishers para enviar dados para os tópicos
        self.movement_publisher = self.create_publisher(Float32MultiArray, 'movement_topic', 2)
        self.imu_publisher = self.create_publisher(Float32, 'imu_topic', 2)

        # Inicializando os valores do vetor de movimento (x, y)
        self.movement_data = [0.0, 0.0]  # x, y são as coordenadas de movimento
        
        # Inicializando a orientação do IMU usando um quaternion
        self.imu_angle = 0.0  # Inicialmente sem rotação em z


        # Inicializando dois ângulos adicionais
        self.angle1 = 0.0

        # Incremento para alterar os valores de movimento e ângulos
        self.step_movement = 10.0  # Quantidade de alteração para o movimento (x, y)
        self.step_angle = 0.2618  # Quantidade de alteração para os ângulos

        # Iniciando o listener para capturar teclas pressionadas
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        # Criando um timer que chamará o método `publish_data` a cada 0.1 segundo
        self.timer = self.create_timer(0.1, self.publish_data)

    # Função para capturar eventos de tecla
    def on_press(self, key):
        try:
            # Verifica qual tecla foi pressionada e altera o movimento ou o ângulo correspondente
            if key.char == 'w':
                self.movement_data[0] = self.step_movement  # Aumenta o valor de x (movimento para frente)
            elif key.char == 's':
                self.movement_data[0] = -self.step_movement  # Diminui o valor de x (movimento para trás)
            elif key.char == 'a':
                self.movement_data[1] = -self.step_movement  # Diminui o valor de y (movimento para a esquerda)
            elif key.char == 'd':
                self.movement_data[1] = self.step_movement  # Aumenta o valor de y (movimento para a direita)

            # Teclas Q/E alteram o valor de rotação no eixo z do IMU
            elif key.char == 'q':
                self.imu_angle+=self.step_angle  # Aumenta o ângulo da robô no eixo z
            elif key.char == 'e':
                self.imu_angle-=self.step_angle  # Diminui o ângulo da robô no eixo z

            # Teclas Z/X alteram o ângulo do pescoço (angle2)
            elif key.char == 'z':
                self.angle1 += self.step_angle  # Aumenta o primeiro ângulo
            elif key.char == 'x':
                self.angle1 -= self.step_angle  # Diminui o primeiro ângulo



        except AttributeError:
            pass

    # Função para publicar os dados de movimento e IMU
    def publish_data(self):
        # Publica os dados de movimento (coordenadas x e y + ângulos adicionais)
        movement_msg = Float32MultiArray()
        movement_msg.data = [self.movement_data[0], self.movement_data[1], self.angle1]  # Adiciona os dois ângulos ao final do vetor de movimento (x, y, angle1, angle2)
        self.movement_publisher.publish(movement_msg)
        self.get_logger().info(f'Movimento publicado: {movement_msg.data}')  # Log para depuração
        self.movement_data[0], self.movement_data[1] = 0.0,0.0

        # Publica os dados do IMU
        imu_msg = Float32()
        imu_msg.data = self.imu_angle
        self.imu_publisher.publish(imu_msg)
        self.get_logger().info(f'IMU publicado: Uz={self.imu_angle}')  # Log para depuração


def main(args=None):
    # Inicializa o sistema ROS2
    rclpy.init(args=args)

    # Cria a instância do nó
    node = TestPublisher()

    try:
        # Mantém o nó rodando e capturando eventos
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # Destrói o nó e encerra o ROS2
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



    
