#!/usr/bin/env python3
#coding=utf-8

import rclpy, os, sys
from rclpy.node import Node
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import CurrentStateMsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class stand_still_routine(Node):

    def __init__(self):
        super().__init__('stand_still_node')

        self.parameters = BehaviourParameters()
        
        #self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
        #rospy.wait_for_service('/movement_central/request_page')
        self.move_request = self.create_client(Page, '/movement_central/request_page')
        while not self.move_request.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        #rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        self.subscription = self.create_subscription(CurrentStateMsg,'/transitions_and_states/state_machine',self.flag_update,10)
        

        self.flag = False 
        #rospy.Timer(rospy.Duration(self.parameters.timerFirstPose), self.runStandStill)
        self.timer = self.create_timer(self.parameters.timerFirstPose, self.run_stand_still)


    def runStandStill(self, event):
        if self.flag:
            print('Routine Stand Still')
            self.move_request('aurea_first_pose')
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'stand_still':
            self.flag = True
        else:
            self.flag = False


'''if __name__ == '__main__':
    rospy.init_node('stand_still_node', anonymous=False)

    routine = stand_still_routine()
    rospy.spin()
    '''

def main(args=None):
    rclpy.init(args=args)
    routine = stand_still_routine()
    rclpy.spin(routine)
    routine.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()