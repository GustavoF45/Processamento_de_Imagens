import numpy as np
import cv2 as cv

frame = cv.imread('img.png')

hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

low_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])

mask = cv.inRange(hsv, low_red, upper_red)

res = cv.bitwise_and(frame,frame, mask= mask)

cv.imshow('frame',frame)
cv.imshow('mask',mask)
cv.imshow('res',res)

