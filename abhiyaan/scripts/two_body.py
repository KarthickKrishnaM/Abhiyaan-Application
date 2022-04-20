#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

'''
Initial conditions considered:
mass of turtle1 = m
mass of turtle2 = 4m
Value of G*m = 1
Initial velocities of both turtles point in opposite directions and are such that the revolve in concentric circles about their centre of mass with same angular velocity.
(v1=4*sqrt(Gm/0.2r) v2=sqrt(Gm/0.2r) where r is the separation between the turtles at given instant) 
In initial setup, the separation between the turtles is 5 units. This setup is done separately in the terminal.
Since we are fixing linear and angular velocities based on instantaneous separations, small fluctuations cause the radius of orbit to decrease/increase over time. This creates a spiral like pattern.
But as they still have equal angular velocities, they will always point in opposite directions and have equal time periods.

'''

x1,y1,x2,y2=0,0,0,0 #coordinates of turtle1 and turtle2
def callback1(data):
    global x1
    global y1
    x1=data.x #updating position of turtle1
    y1=data.y
def callback2(data):
    global x2
    global y2 
    x2=data.x #updating position of turtle1
    y2=data.y 
def move():
    rospy.init_node('turtlesim', anonymous=True) #initialising node
    #to publish velocity messages to each turtle
    vel_publisher1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_publisher2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    #to get pose information of each turtle
    rospy.Subscriber("/turtle1/pose", Pose, callback1)
    rospy.Subscriber("/turtle2/pose", Pose, callback2)
    
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
    	vel_msg1 = Twist() #velocity message for turtle1
    	vel_msg2 = Twist() #velocity message for turtle2
    	distance=math.sqrt((x2-x1)**2+(y2-y1)**2) #distance between the turtles
    	if distance!=0:
    		vel_msg1.linear.x=4*math.sqrt(5/distance) #since the turtles always moves tangential to the orbit, only x component of linear velocity and z component of angular velocity is non zero
    		vel_msg2.linear.x=math.sqrt(5/distance)
    		vel_msg1.linear.y,vel_msg2.linear.y=0,0
    		vel_msg1.linear.z,vel_msg2.linear.z=0,0
    		vel_msg1.angular.x,vel_msg2.angular.x=0,0
    		vel_msg1.angular.y,vel_msg2.angular.y=0,0
    		vel_msg1.angular.z,vel_msg2.angular.z=math.sqrt((5/distance)**3),math.sqrt((5/distance)**3)
    	vel_publisher1.publish(vel_msg1)
    	vel_publisher2.publish(vel_msg2)
    	rate.sleep()
if __name__ == '__main__':
    
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException:
        pass
