# coding=utf-8

import rospy

import src.game_mode as game_mode
import src.test_mode as test_mode

def main(args):

    gm = game_mode.GameModeFinder()
    tm = test_mode.TestModeFinder()

    rospy.init_node('object_finder', anonymous=True)

    if rospy.has_param("game_mode"):
        game = rospy.get_param("game_mode")
    else:
	    game = False


    try:
        if game == True:
            gm.game_mode()
            rospy.spin()
        else:
            tm.live_mode()
    except rospy.ROSInterruptException:
        print('Exception')
