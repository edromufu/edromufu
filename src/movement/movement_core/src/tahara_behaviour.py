#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import rospy, os, sys
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

# Scan rectangle limits and pacing
UP_Y_POSITION = 0.0
BOTTOM_Y_POSITION = -0.95
LEFT_X_POSITION = 1.15
RIGHT_X_POSITION = -1.15
X_STEPS = 30
Y_STEPS = 10
TIME_NS = int(2e8)  # 0.2 s in nanoseconds

class CoreHead:
    def __init__(self):
        rospy.init_node('head_central')

        self.parameters = BehaviourParameters()

        # Feedback + head motor publisher
        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2head', head_motors_data, queue_size=10)
        self.pub2motorsMsg = head_motors_data()

        # Vision
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters)

        # Motion controller (page caller) — used for the reaction
        rospy.wait_for_service('movement_central/request_page')
        self.pageCall = rospy.ServiceProxy('movement_central/request_page', page)

        # --- State ---
        self.found = False
        self.hasReceivedVision = False
        self.timesFoundFalse = 0
        self.x = 0
        self.y = 0

        # Reaction config (name WITHOUT .json is typical)
        self.reaction_page = rospy.get_param('~goalkeeper_json_name', 'tahara_goalkeeper_pose')
        self.reaction_cooldown = rospy.Duration.from_sec(rospy.get_param('~reaction_cooldown_s', 1.0))
        self.lastReaction = rospy.Time(0)
        self.was_found = False  # track rising edge: not found -> found

        # Scan timing
        self.scanInterval = rospy.Duration(nsecs=TIME_NS)

        # Precompute clockwise rectangle path
        self.defineSearchPattern()

    # ----------------- pattern -----------------
    def defineSearchPattern(self):
        x_top_cw   = np.linspace(LEFT_X_POSITION,  RIGHT_X_POSITION, X_STEPS)
        y_right_cw = np.linspace(UP_Y_POSITION,    BOTTOM_Y_POSITION, Y_STEPS)
        x_bot_cw   = np.linspace(RIGHT_X_POSITION, LEFT_X_POSITION,  X_STEPS)
        y_left_cw  = np.linspace(BOTTOM_Y_POSITION,UP_Y_POSITION,    Y_STEPS)

        top_cw    = np.c_[x_top_cw,   np.full_like(x_top_cw,   UP_Y_POSITION)]
        right_cw  = np.c_[np.full_like(y_right_cw, RIGHT_X_POSITION), y_right_cw]
        bottom_cw = np.c_[x_bot_cw,   np.full_like(x_bot_cw,   BOTTOM_Y_POSITION)]
        left_cw   = np.c_[np.full_like(y_left_cw,  LEFT_X_POSITION),  y_left_cw]

        self.cwHeadPositions = np.concatenate((top_cw, right_cw, bottom_cw, left_cw))

    # ----------------- vision ------------------
    def updateBallParameters(self, msg):
        ball = msg.ball
        if not ball.found:
            self.timesFoundFalse += 1
            if self.timesFoundFalse >= 3:
                self.found = False
                self.timesFoundFalse = 0
        else:
            self.found = True
            self.x = ball.x
            self.y = ball.y
            self.timesFoundFalse = 0
            self.hasReceivedVision = True

    # ----------------- main loop ---------------
    def run(self):
        lastScan = rospy.Time.now()
        justLostTheBall = True  # first step after loss
        i = 0                   # scan index
        rotation = 1            # scan direction

        rate = rospy.Rate(60)   # high-rate loop; actions paced by durations
        while not rospy.is_shutdown():
            now = rospy.Time.now()

            if self.found:
                # On the RISING EDGE (lost -> found) OR cooldown passed: trigger reaction
                if (not self.was_found) or ((now - self.lastReaction) >= self.reaction_cooldown):
                    try:
                        # Call the motion controller with the page name (JSON-backed)
                        self.pageCall(self.reaction_page)
                        self.lastReaction = now
                    except rospy.ServiceException as e:
                        rospy.logwarn("Failed to call reaction page '%s': %s",
                                      self.reaction_page, str(e))

                # We’re in found mode; reset scanning state for when we lose it
                self.hasReceivedVision = False
                justLostTheBall = True
                self.was_found = True

            else:
                # Not found: rectangle scan continues
                if justLostTheBall:
                    # Choose direction based on last known x (kept from previous detections)
                    rotation = 1 if self.x > self.parameters.xCenterRightLimit else -1

                    # Start from nearest waypoint to current head pose (no sudden jump)
                    try:
                        currentHor, currentVer = self.motorsFeedback(True).pos_vector
                    except rospy.ServiceException as e:
                        rospy.logwarn("Head feedback failed: %s", str(e))
                        currentHor, currentVer = 0.0, 0.0

                    dists = np.hypot(self.cwHeadPositions[:,0] - currentHor,
                                     self.cwHeadPositions[:,1] - currentVer)
                    i = int(np.argmin(dists))
                    justLostTheBall = False

                # Step the scan at fixed interval
                if (now - lastScan) >= self.scanInterval:
                    self.pub2motorsMsg.pos_vector = self.cwHeadPositions[i].tolist()
                    self.pub2motors.publish(self.pub2motorsMsg)
                    i = (i + rotation) % len(self.cwHeadPositions)
                    lastScan = now

                self.was_found = False  # we’re currently in “not found”

            rate.sleep()

if _name_ == '__main__':
    node = CoreHead()
    node.run()
    rospy.spin()