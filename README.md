# Highway2Hole

![logo](https://github.com/DumDereDum/Highway2Hole/blob/main/img/logo.png)

## Overview / Usage

The invention of automobiles over the years has changed people's lives in many ways. Automobiles have greatly revolutionized the way people move and deliver things from one place to the other. Besides cars has become a hobby for millions of people, they watch or do racing, reconstruct old cars and collect them.

When we are talking about automobiles we must not forget about roads and their existence alone will not be enough. We need to estimate their quality and safety. The main characteristics of quality are road defects, markings, and curb condition. Highway2Hole helps you to avoid potholes and poor-quality roads to move safely and keep your car serviceable.

## Methodology / Approach

Highway2Hole uses Intel OpenVINO™’ for inference of model which finds defects on the roads. It uses pre-trained model yolov3-road-damage-detection. Firstly, the user takes the video and GPS data from the car. Then model finds frames with road damage and logs them. After all logs are ready, the program matches frames and locations and pushes them to the database. Information from db is used later to mark potholes on the map.

Solving tasks of object detection is implemented in the separate class named Detector. This class was created due to Open Model Zoo and OpenVino IE class organization approach. The pipeline is shown below:

1) Creation of IE Core for controlling available devices and reading net objects.

2) Uploading of the pre-trained model which is in IR format, getting information about topology configuring input and output data to occur in the class constructor.

3) Infer Request is created and Infer starts up.

In future versions, we are going to use more powerful devices to get clean data from cars in real-time. In addition, we will add the version for cyclists. It would be also useful to add a navigator which will try to avoid congestions of potholes.
