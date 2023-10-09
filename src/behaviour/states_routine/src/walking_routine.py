#!/usr/bin/env python3
#coding=utf-8

import rospy, os, sys
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import currentStateMsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class WalkingRoutine():

    def __init__(self):
        self.parameters = BehaviourParameters()

        self.move_request = rospy.ServiceProxy('/movement_central/request_walk', walk_forward)
        rospy.wait_for_service('/movement_central/request_walk')

        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.supFoot = 1
        self.stepNumber = 6

        self.flag = False
        rospy.Timer(rospy.Duration(self.parameters.timerWalk), self.runWalk)

    def runWalk(self, event):
        print('Walking')
        if self.flag:
            print(self.stepNumber)
            self.move_request(self.supFoot, self.stepNumber)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'walking':
            self.flag = True
            self.runWalk(True)
        else:
            self.flag = False


if __name__ == '__main__':
    rospy.init_node('walking_node', anonymous=False)

    routine = WalkingRoutine()
    rospy.spin()