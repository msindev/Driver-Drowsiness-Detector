[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20Driver%20Drowsiness%20Detection%20project%20on%20Github%20&url=https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/&hashtags=python,drowsiness-detector,opencv,computer-vision,machine-learning,deep-learning)  [![GitHub stars](https://img.shields.io/github/stars/mohitwildbeast/Driver-Drowsiness-Detector.svg?style=plastic)](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/stargazers)  [![GitHub forks](https://img.shields.io/github/forks/mohitwildbeast/Driver-Drowsiness-Detector.svg?style=plastic)](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/network)



This program is used to detect drowsiness for any given person. In this program we check how long a person's eyes have been closed for. If the eyes have been closed for a long period i.e. beyond a certain threshold value, the program will alert the user by playing an alarm sound.

The program contains 3 files, which are
## Files
 - **face_and_eye_detector_single_image.py** - Detects face and eye from a single image.
 Demo-
 
|  ![Test Image](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/blob/master/images/test.jpeg)| ![Result Image](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/blob/master/images/result_face_detector_single_image.png) |
|---|---|

 - **face_and_eye_detector_webcam_video.py** - Detects face and eye in a webcam feed by user![Webcam Face and Eye Detection](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/blob/master/images/webcam_face_eye_detect.jpeg)
 - **drowsiness_detect.py**- This script detects if person is drowsy or not using webcam video feed

> DEMO
![Drowsiness Detection Demo](https://github.com/mohitwildbeast/Driver-Drowsiness-Detector/blob/master/images/drowsiness_detector_demo.gif)
 
 ## Requirements
> 
> IMPORTANT

  Download `shape_predictor_68_face_landmarks.dat.bz2` from [Shape Predictor 68 features](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) 
  Extract the file in the project folder using 
  ``bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2``


    numpy==1.15.2
	dlib==19.16.0
	pygame==1.9.4
	imutils==0.5.1
	opencv_python==3.4.3.18
	scipy==1.1.0
Use `pip install -r requirements.txt`to install the given requirements.

## Usage

### Detect Face and Eyes in a Single Image
Put your file to be detected in **images** folder with name **test.jpeg** or change the file path in `Line : 14 face_and_eye_detector_single_image.py` to your image file.                     
Run script using:

    python face_and_eye_detector_single_image.py

### Detect Face and Eyes in a Webcam Feed
Run script using:

    python face_and_eye_detector_webcam_video.py
### Drowsiness Detection
Run script using:

    python drowsiness_detect.py

The algorithm for Eye Aspect Ratio was taken from pyimagesearch.com blog, by Adrian RoseBrock.
