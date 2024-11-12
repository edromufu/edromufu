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

class WalkingRoutine():

    def __init__(self):
        super().__init__('walking_node')
        self.parameters = BehaviourParameters()

        #self.move_request = rclpy.ServiceProxy('/movement_central/request_walk', walk_forward)
        #rclpy.wait_for_service('/movement_central/request_walk')
        self.move_request = self.create_client(WalkForward, '/movement_central/request_walk')
        while not self.move_request.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        #rclpy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        self.subscription = self.create_subscription(CurrentStateMsg,'/transitions_and_states/state_machine',self.flag_update,10)

        self.supFoot = 1
        self.stepNumber = 6

        self.flag = False
        #rclpy.Timer(rclpy.Duration(self.parameters.timerWalk), self.runWalk)
        self.timer = self.create_timer(self.parameters.timerWalk, self.run_walk)

    def runWalk(self, event):
        if self.flag:
            print('Routine Walk')
            #self.move_request(self.supFoot, self.stepNumber)
            request = WalkForward.Request()
            request.sup_foot = self.supFoot
            request.step_number = self.stepNumber
            self.move_request.call_async(request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'walking':
            self.flag = True
        else:
            self.flag = False


'''if __name__ == '__main__':
    rclpy.init_node('walking_node', anonymous=False)

    routine = WalkingRoutine()
    rclpy.spin()
    '''
def main(args=None):
    rclpy.init(args=args)
    routine = WalkingRoutine()
    rclpy.spin(routine)
    routine.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()