#! /usr/bin/env python
import rospkg
import rospy
from turtlebot_move.srv import MoveDirection, MoveDirectionRequest


rospy.init_node('turtlebot_move_service_client') # Initialise a ROS node with the name turtlebot_move_service_client
rospy.wait_for_service('/move_direction') # Wait for the service client /move_bb8_in_circle_custom to be running
turtlebot_move_service_client = rospy.ServiceProxy('/move_direction', MoveDirection) # Create the connection to the service
turtlebot_move_request_object = MoveDirectionRequest() # Create an object of type MoveDirectionRequest


"""
# the string that indicates which direction to take
int32 repetitions  
---
bool complete         # Did it achieve it?
"""

turtlebot_move_request_object.direction = 'right'

rospy.loginfo("Doing Service Call...")
result = turtlebot_move_service_client(turtlebot_move_request_object) # Send through the command to be executed
rospy.loginfo(str(result)) # Print the result given by the service called

rospy.loginfo("END of Service call...")
