
#  |======================================================|
#  |                                                      |
#  | Publisher dos Potenciometros                         |
#  | Feito por Pedro H. Peres caso alguma dúvida ou erro  |
#  |                                                      |
#  |======================================================|

import sys, json, os
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement/movement_pages/pages_tahara/'

class pagePublisher(Node):

    def __init__(self):
        super().__init__('page_publisher')
                       
        self.pageName = self.declare_parameter('movement/page',None).get_parameter_value().string_value
        self.publisher_ = self.create_publisher(Float32MultiArray, 'pot_py_topic', 10)
        timer_period = 3  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.timer_callback()

        
    def timer_callback(self):
        msg = Float32MultiArray()
        with open(MAIN_DIR+'Page1.json', 'r') as pageFile:
            jsonData = json.loads(pageFile.read())
            
        for j in range(len(jsonData['joints_positions']['pot_0'])):
            values = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0] 
            k=0
            for i in jsonData['joints_positions']:
                print(k,i,j)
                values[k]=jsonData['joints_positions'][i][j]
                k+=1
                # Aqui entra os valores dos potenciometros
                msg.data = values
                #for i, value in enumerate(values, start=1):
                #   setattr(msg, f'pot{i}', value)     
                
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing')


def main(args=None):
    rclpy.init(args=args)

    page_publisher = pagePublisher()

    rclpy.spin(page_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    page_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
