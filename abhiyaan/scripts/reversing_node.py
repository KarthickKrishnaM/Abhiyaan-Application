#!/usr/bin/env python
import rospy
from std_msgs.msg import String
string=''
def callback(data):
    global string
    string=str(data.data)

def publisher():
    pub = rospy.Publisher('naayihba_maet', String, queue_size=10)
    rospy.init_node('reversing_node', anonymous=True)
    rospy.Subscriber("team_abhiyaan", String, callback)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	reverse=''
    	for i in string.split():
    		reverse+=i[::-1]+' '
    	rospy.loginfo(reverse)
    	pub.publish(reverse)
    	rate.sleep()
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

