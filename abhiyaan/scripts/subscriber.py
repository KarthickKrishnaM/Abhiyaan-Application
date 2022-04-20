#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)
    
def subscriber():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("team_abhiyaan", String, callback) #subscribing to required topic

    # keep python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
