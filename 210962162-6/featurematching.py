import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread('Resources/munch-chocolate.jpg',cv.IMREAD_GRAYSCALE) # queryImage
img2 = cv.imread('Resources/IMG_20210303_122309.jpg',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Apply ratio test
good = []
for m,n in matches:
 if m.distance < 0.75*n.distance:
    good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()

# https://medium.com/@russmislam/implementing-sift-in-python-a-complete-guide-part-1-306a99b50aa5#:~:text=In%20this%20tutorial%2C%20we%E2%80%99ll%20walk%20through%20this%20code,and%20Pythonizing%20the%20logic%20without%20sacrificing%20any%20details.