# dnt_ros_task1

The goal is to create a ROS-based system that demonstrates the concept of
publish/subscribe communication with an added twist of message encryption and decryption.
This system will consist of three parts:
1. pub.py: A ROS publisher node that encrypts a string (your name) using the Caesar
cipher and publishes it on a ROS topic.
2. pubsub.py: A ROS node that acts both as a subscriber and a publisher. It
subscribes to the topic from pub.py, decrypts the encrypted name, and then
publishes the decrypted name onto a new ROS topic.
3. sub.py: A ROS subscriber node that listens to the final topic from pubsub.py and
prints out the decrypted name

Procedure to run the code:
1. Run roscore
2. Source `<workspace_name>/devel/setup.bash`
3. Make pub.py, pubsub.py and sub.py executable using the command ` chmod +x <filename>`
4. Run each file using ` rosrun <pkg_name> <filename>`
