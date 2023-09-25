#!/usr/bin/env python3
# Author:Sanjay J P

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

def webcam_publisher():
    rospy.init_node('webcam_publisher', anonymous=True)
    rate = rospy.get_param('~publish_rate', 10) 
    image_pub = rospy.Publisher('webcam/image_raw', Image, queue_size=1)
    cap = cv2.VideoCapture(0)
    bridge = CvBridge()

    rate = rospy.Rate(rate)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            img_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_pub.publish(img_msg)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass
