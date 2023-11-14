#!/usr/bin/python3
import rospy
from std_msgs.msg import String

# idk how this codeblock works but it just does
def encrypt(word, shift):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            encrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word

rospy.init_node("encrypting_node",anonymous=False)

the_talker = rospy.Publisher("/encrypted_name", String, queue_size=10)

rate = rospy.Rate(1)


# encryped words are published onto pubsub.py
while not rospy.is_shutdown():
    word="amrit"

    encrypted_word = encrypt(word, shift=1)


    the_talker.publish(encrypted_word)
    rate.sleep()
    