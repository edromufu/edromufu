#!/usr/bin/env python3
#coding=utf-8

import rclpy, os, sys
from rclpy.node import Node
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import StateMachineMsg
from modularized_bhv_msgs.msg import CurrentStateMsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class getting_up_routine(Node):

    def __init__(self):
        super().__init__('getting_up_node')
        self.parameters = BehaviourParameters()

        #self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
        self.move_request = self.create_client(Page, '/movement_central/request_page')
        #rospy.wait_for_service('/movement_central/request_page')
        while not self.move_request.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        #rospy.Subscriber(self.parameters.stateMachineTopic, stateMachineMsg, self.fallStatusUpdate)
        #rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        self.create_subscription(StateMachineMsg, self.parameters.stateMachineTopic, self.fall_status_update, 10)
        self.create_subscription(CurrentStateMsg, '/transitions_and_states/state_machine', self.flag_update, 10)
        

        self.flag = False
        self.currentGetUpPage = None
        
        #rospy.Timer(rospy.Duration(self.parameters.timerPage), self.runGetUp)
        self.timer = self.create_timer(self.parameters.timerPage, self.run_get_up)

    def runGetUp(self, event):
        if self.flag:
            print('Routine Get Up') 
            #self.move_request(self.currentGetUpPage)
            request = Page.Request() 
            request.page_name = self.current_get_up_page # Variável 'page' inventada pelo GPT
            self.move_request.call_async(request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'getting_up':
            self.flag = True
        else:
            self.flag = False

    def fallStatusUpdate(self,msg):
        
        if msg.fallState == self.parameters.left or msg.fallState == self.parameters.right or msg.fallState == self.parameters.back:
            self.currentGetUpPage = 'aurea_get_up_back'
        elif msg.fallState == self.parameters.front:
            self.currentGetUpPage = 'aurea_get_up_front'

'''if __name__ == '__main__':
    rospy.init_node('getting_up_node', anonymous=False)

    routine = getting_up_routine()
    rospy.spin()
    '''
def main(args=None):
    rclpy.init(args=args)
    routine = getting_up_routine()
    rclpy.spin(routine)
    routine.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()