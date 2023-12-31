# GUI_rosbag_webcam_recorder
### Overview:
This repository contains code and resources for a ROS (Robot Operating System) noetic project that captures video from a webcam and publishes it as a ROS topic while providing functionality to record the data as a ROS bag file , play back the saved file or live video stream.


![Screenshot from 2023-09-25 14-32-52](https://github.com/Sanjay-j-p/GUI_rosbag_webcam_recorder/assets/11870995/a427334f-93dd-4cfc-b4a4-c0f19436c490)


### Features:

    Webcam Streaming: Utilizes OpenCV and ROS to stream video from your webcam to a ROS topic.
    ROS Bag Recording: Allows you to record the webcam stream as a ROS bag file for later analysis and to view the recorded bag.
    User-Friendly GUI: Provides a simple graphical user interface (GUI) for starting and stopping webcam streaming and recording.
    Customization: Easily configurable and adaptable to different webcam configurations and ROS setups.

### Dependencies:

    ROS 1 
    OpenCV
    Python 3

### Usage:

1.Clone this repository to your ROS workspace.

    git clone https://github.com/Sanjay-j-p/GUI_rosbag_webcam_recorder.git

2.Build the ROS package using catkin_make.

    catkin_make or catkin build
    
3.Run Roscore

    roscore

3.Run the GUI script to see the above metioned features    

    rosrun webcam_recorder gui.py 

### Contributions:
Contributions and improvements to the project are welcome! Feel free to fork this repository, make changes, and submit pull requests.

### License:
This project is licensed under the MIT License.

### Author:
Sanjay J P
mrsanjayjp@gmail.com


