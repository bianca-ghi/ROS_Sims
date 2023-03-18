#! /usr/bin/env python3

# This is where you will publish the velocity messages to the turtlebot and subscribe to its laserscan data.


import rospy  # Import the Python library for ROS_msgs package
from sensor_msgs.msg import LaserScan
from turtlebot_make_square.srv import MoveInSquare, MoveInSquareResponse, MoveInSquareRequest
import sys

rospy.init_node('turtlebot_demo')  # Initiate a Node

rospy.wait_for_service('/move_in_square')
move_in_square = rospy.ServiceProxy('/move_in_square', MoveInSquare)

move_in_square_object = MoveInSquareRequest()
complete = move_in_square(move_in_square_object)
