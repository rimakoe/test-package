#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

class TestPackage:
    def __init__(self):
        # Create publisher
        self.ackermann_publisher = rospy.Publisher('/ackermann_cmd', AckermannDriveStamped, queue_size=1) 

    def do_stuff(self):
        # Generate artificial data
        ackermann_message = AckermannDriveStamped()
        ackermann_message.header.stamp = rospy.Time.now()
        ackermann_message.drive.steering_angle = 0
        ackermann_message.drive.speed = 0
        # publish the data
        self.ackermann_publisher.publish(ackermann_message)
        
if __name__ == '__main__':
    rospy.init_node('test_package', anonymous=True)
    
    test_package = TestPackage()
    
    while not rospy.is_shutdown():
        try:
            test_package.do_stuff()
            rospy.sleep(1)
        except KeyboardInterrupt:
            print("Interrupted. Shutting down...")