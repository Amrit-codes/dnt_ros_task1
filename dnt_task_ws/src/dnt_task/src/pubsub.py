#!/usr/bin/python3
import rospy
from std_msgs.msg import String

#it just works!!!
def decrypt(encrypted_word, shift):
    decrypted_word = ""
    for char in encrypted_word:
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            decrypted_word += decrypted_char
        else:
            decrypted_word += char
    return decrypted_word


rospy.init_node("decrypting_and_republishing",anonymous=False)


def callback(msg):
    # subscribes the decrypted messages
    msg.data = decrypt(msg.data, shift=1)
    # print(msg.data)
    #republishes the decrypted messages
    decrypted_publisher.publish(msg.data)


the_listener= rospy.Subscriber("/encrypted_name", String, callback)

decrypted_publisher = rospy.Publisher("/decrypted_name", String, queue_size=10)

rospy.spin()

