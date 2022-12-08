#!/usr/bin/env python

from behaviour_msgs.srv import service_page
import rospy

def handle(req):

    print (req.page)
    return req.page

def server():

    rospy.init_node('server')
    s = rospy.Service('/humanoid_qt/movecreator_qt/page', service_page, handle)
    print ("ready to get msg")
    rospy.spin()

if __name__ == "__main__":
    server()
