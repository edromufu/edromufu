#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import CurrentStateMsg


class KickRoutine(Node):

    def __init__(self):
        super().__init__('kick_node')
        
        #self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
        self.move_request = self.create_client(Page, '/movement_central/request_page')
        #rospy.wait_for_service('/movement_central/request_page')
        while not self.move_request.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        #rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        self.subscription = self.create_subscription(CurrentStateMsg, '/transitions_and_states/state_machine', self.flag_update, 10)

        self.flag = False
        self.last_decision = None

        self.timer = self.create_timer(0.1, self.process_request) #Executa a função self.process_request a cada 0.1sec

        #Essa parte se tornou uma função process_request
        '''while not rospy.is_shutdown():
            self.createRequest()

            if self.last_decision != self.request:
                self.last_decision = self.request
                self.move_request(self.request)
                '''

    def process_request(self):
        self.create_request()

        if self.last_decision != self.request:
            self.last_decision = self.request
            if self.request:
                request = Page.Request()
                request.page = self.request
                self.move_request.call_async(request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'kick':
            self.flag = True
        else:
            self.flag = False

        
    def createRequest(self):
        
        if self.flag:
            self.request = f'aurea_kick'
        else:
            self.request = None


'''if __name__ == '__main__':
    rospy.init_node('Kick_node', anonymous=False)

    routine = KickRoutine()
    rospy.spin()
    '''

def main(args=None):
    rclpy.init(args=args)
    routine = KickRoutine()
    rclpy.spin(routine)
    routine.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()