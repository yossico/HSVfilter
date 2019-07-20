import numpy as np
import cv2


# Load an color image in grayscale
img = cv2.imread('frame111.jpg')
cv2.imshow('orig',img )

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([0.87*179, 0, 0.79*255])
upper_blue = np.array([179, 0.11*255, 255])
# Threshold the HSV image to get only blue colors
mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

lower_blue = np.array([0, 0, 0.79*255])
upper_blue = np.array([0.15*179, 0.11*255, 255])
# Threshold the HSV image to get only blue colors
mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

mask = cv2.bitwise_or(mask1 ,mask2)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img ,img, mask= mask)

cv2.imshow('frame' ,img)
cv2.imshow('mask' ,mask)
cv2.imshow('res' ,res)
cv2.waitKey(0)