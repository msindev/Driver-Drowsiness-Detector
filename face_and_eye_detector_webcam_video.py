'''This script uses OpenCV's haarcascade (face and eye cascade) to detect face
and eyes in a video feed which can be inputted through a webcam.'''

#Import necessary libraries
import cv2 as cv
import numpy as np

#Load face cascade and hair cascade from haarcascades folder
face_cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")

#Capture video from webcam
video_capture = cv.VideoCapture(0)

#Read all frames from webcam
while True:
    ret, frame = video_capture.read()
    frame = cv.flip(frame,1) #Flip so that video feed is not flipped, and appears mirror like.
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv.imshow('Video', frame)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

#Finally when video capture is over, release the video capture and destroyAllWindows
video_capture.release()
cv.destroyAllWindows()
