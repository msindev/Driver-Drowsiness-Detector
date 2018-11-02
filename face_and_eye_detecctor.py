'''This script uses OpenCV's haarcascade (face and eye cascade) to detect face
and eyes in a video feed which can be inputted through a webcam.'''

import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontal_face_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread('images/mohit.jpeg')

faces = face_cascade.detectMultiScale(img, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)
    roi = img[y:y+h, x:x+w]

    #Only when a face is detected eyes will be present, so it is placed in loop
    eyes = eye_cascade.detectMultiScale(roi)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi, (ex, ey), (ex+w, ey+h), (0,255,0), 2)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
