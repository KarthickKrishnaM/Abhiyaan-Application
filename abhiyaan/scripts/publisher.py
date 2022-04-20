#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10) #publishing to required topic
    rospy.init_node('publisher', anonymous=True)    #initializing node
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        string = "Team Abhiyaan rocks:"
        rospy.loginfo(string) #printing published data to terminal
        pub.publish(string)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
