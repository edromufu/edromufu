import rclpy
from rclpy.node import Node

from potmessage.msg import Potmsg


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Potmsg, 'pot_mess_sub', 10)  
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.subscription = self.create_subscription(Potmsg,'micro_ros_publisher',self.listener_callback,10)
        self.subscription
        
    def timer_callback(self):
        msg = Potmsg()                                                
        msg.pot1 = self.i                                           
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.pot1)       
        self.i += 1

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.pot1)  


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
