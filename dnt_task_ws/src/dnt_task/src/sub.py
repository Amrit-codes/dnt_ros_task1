#!/usr/bin/python3
import rospy
from std_msgs.msg import String

rospy.init_node("final_subscriber",anonymous=False)

def callback(msg):
    # prints the decrypted string
    print(msg.data)

the_listener= rospy.Subscriber("/decrypted_name", String, callback)

rospy.spin()
