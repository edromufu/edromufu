
#  |======================================================|
#  |                                                      |
#  | Publisher dos Potenciometros                         |
#  | Feito por Pedro H. Peres caso alguma dúvida ou erro  |
#  |                                                      |
#  |======================================================|


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'pot_py_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32MultiArray()
        values = [500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0] # Aqui entra os valores dos potenciometros
        msg.data = values
        #for i, value in enumerate(values, start=1):
         #   setattr(msg, f'pot{i}', value)     
        
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
