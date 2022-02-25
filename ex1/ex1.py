import numpy as np
import cv2

img1 = cv2.imread('img1.jpg')

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret,thresh_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv2.imwrite('img2.png', thresh_img)

img2 = cv2.imread('img2.png')

img_concats = np.concatenate((img1, img2), axis=1)

cv2.imshow('Black and White (Binary)', img_concats)

