#!/usr/bin/env python3

import rospy
import tkinter as tk
import subprocess
from datetime import datetime
from tkinter import filedialog
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import threading
import cv2
rosbag_process = None
bag_file = None
playing = False
window_closed = False
cap = None 
def choose_bag_file():
    global bag_file
    bag_file = filedialog.askopenfilename(filetypes=[("ROS Bag Files", "*.bag")])

def play_bag():
    global bag_file, playing, window_closed

    if bag_file is None:
        print("Please choose a ROS bag file first.")
        return

    bag = rosbag.Bag(bag_file, "r")
    bridge = CvBridge()

    for _, msg, _ in bag.read_messages(topics=['/webcam/image_raw']):
        if not playing or window_closed:
            break

        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        cv2.imshow("ROS Bag Playback", frame)
        key = cv2.waitKey(100)  # Adjust the playback speed as needed

        # Check if the window close event (X button) was triggered
        # if key == 27 or key == ord('q'):  # ESC key or 'q' key
            # window_closed = True
            # break

    bag.close()
    playing = False
    cv2.destroyAllWindows()

def play_button_callback():
    global playing
    if playing:
        playing = False
    else:
        playing = True
        play_thread = threading.Thread(target=play_bag)
        play_thread.start()
def start_recording():
    global rosbag_process
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    bag_file_name = f"webcam_{current_time}.bag"
    rosbag_process = subprocess.Popen(['rosbag', 'record', '-O', bag_file_name, '/webcam/image_raw'])

def stop_recording():
    global rosbag_process
    if rosbag_process:
        rosbag_process.terminate()
        rosbag_process.wait()
        rosbag_process = None
def start_live_stream():
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)  # Open the default camera (usually webcam)

    while True:
        ret, frame = cap.read()

        if not ret or window_closed:
            break

        cv2.imshow("Live Stream", frame)
        key = cv2.waitKey(100)  # Adjust the playback speed as needed

        # Check if the window close event (X button) was triggered or 'q' key pressed
        if key == 27 or key == ord('q'):
            break

    if cap is not None:
        cap.release()
        cap = None
    cv2.destroyAllWindows()


def start_webcam_stream():
    subprocess.Popen(['roslaunch', 'webcam_recorder', 'web.launch'])

def stop_webcam_stream():
    subprocess.call(['rosnode', 'kill', '/webcam_publisher'])



if __name__ == '__main__':
    rospy.init_node('webcam_gui', anonymous=True)
    root = tk.Tk()
    root.title("Webcam Streaming and Recording")

    start_button = tk.Button(root, text="Start Webcam Stream", command=start_webcam_stream)
    stop_button = tk.Button(root, text="Stop Webcam Stream", command=stop_webcam_stream)
    start_record_button = tk.Button(root, text="Start Recording", command=start_recording)
    stop_record_button = tk.Button(root, text="Stop Recording", command=stop_recording)

    choose_button = tk.Button(root, text="Choose ROS Bag File", command=choose_bag_file)
    play_button = tk.Button(root, text="Play/Stop", command=play_button_callback)
    start_live_stream_button = tk.Button(root, text="Play Live Stream", command=start_live_stream)

    
    start_live_stream_button.pack()
    
   
    start_button.pack()
    stop_button.pack()
    start_record_button.pack()
    stop_record_button.pack()
    choose_button.pack()
    play_button.pack()
    root.mainloop()
