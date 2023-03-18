#! /usr/bin/env python3
import rospy
from math import sqrt
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from turtlebot_make_square.srv import MoveInSquare, MoveInSquareResponse

def my_callback(request):
    response = MoveInSquareResponse()
    verif = make_square(0.25)
    if not verif:
        print('Error! An obstacle was found.')
        response.complete = False
    else:
        response.complete = True

    return response


def new_distance(init_pos):
    crt_odom = rospy.wait_for_message('/odom', Odometry, timeout=1)
    crt_position = crt_odom.pose.pose.position
    distance = sqrt((crt_position.x - init_pos.x) * (crt_position.x - init_pos.x) +
                   (crt_position.y - init_pos.y)*(crt_position.y - init_pos.y))
    return distance

def move_straight(dist):
    init_odom = rospy.wait_for_message('/odom', Odometry, timeout=1)
    init_position = init_odom.pose.pose.position
    ok = 1
    while dist > new_distance(init_position):
        pub.publish(vel)
        scan_inf = rospy.wait_for_message('/scan', LaserScan, timeout=1)
        if(scan_inf.ranges[90] < 0.2):
            vel.linear.x = 0.0
            print('The robot faced an obstacle')
            ok = 0
            break
    vel.linear.x = 0.0 
    if ok: print('The robot moved straight for 20cm')
    return ok

def make_square(dist):
    ok = 1
    for i in range(4):
        vel.linear.x = 0.1
        terminate = move_straight(dist)
        if not terminate: ok = 0
        else:
            vel.angular.z = -1.57  # 1.57 radians = 90 degrees
            print('90 degree turn')
            for j in range(4):
                pub.publish(vel) # we publish the same message many times because otherwise robot will stop
                rospy.sleep(0.25)
            vel.angular.z = 0
            pub.publish(vel)
    vel.linear.x = 0.0
    return ok 





vel = Twist()  # Create a var of type Twist
vel.linear.x = 0.1  # Move the robot with a linear velocity in the x axis
vel.angular.z = 0.0

rospy.init_node('turtlebot_make_square')
my_service = rospy.Service('/move_in_square', MoveInSquare, my_callback)
# Create a publisher to the topic /cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
