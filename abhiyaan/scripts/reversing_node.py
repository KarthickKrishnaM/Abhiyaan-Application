#!/usr/bin/env python
import rospy
from std_msgs.msg import String
string=''
def callback(data):
    global string
    string=str(data.data) #storing data got from the subscribed topic

def publisher():
    pub = rospy.Publisher('naayihba_maet', String, queue_size=10) #publishing topic
    rospy.init_node('reversing_node', anonymous=True) #initializing node
    rospy.Subscriber("team_abhiyaan", String, callback) #subscribing to required topic
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	reverse=''          #reversing the message received
    	for i in string.split():
    		reverse+=i[::-1]+' '
    	rospy.loginfo(reverse) #printing reverse message to terminal
    	pub.publish(reverse) #publishing new message to required topic
    	rate.sleep()
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

