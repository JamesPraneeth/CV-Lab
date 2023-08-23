import cv2

import numpy as np

from matplotlib import pyplot as plt

# image = cv2.imread("/Resources/pic1.jpg",1)

image_bw = cv2.imread("/Resources/pic1.jpg",0)

# print(image.shape)
# cv2.imshow("Pic",image)
# red = image[:,:,2]
# green = image[:,:,1]
# blue = image[:,:,0]

# image2 = np.zeros((image.shape))
# image3 = np.zeros((image.shape))
# image4 = np.zeros((image.shape))
# print(image_bw.shape)
# print(image2.shape)
# print(image3.shape)
# print(image4.shape)
# image2 = red
# image3 = green
# image4 = blue
# cv2.imwrite("Resources/image2.jpg",image2)
# cv2.imwrite("Resources/image3.jpg",image3)
# cv2.imwrite("Resources/image4.jpg",image4)

hist_eq = cv2.equalizeHist(image_bw)
# hist_eq2 = cv2.equalizeHist(image2)
# hist_eq3 = cv2.equalizeHist(image3)
# hist_eq4 = cv2.equalizeHist(image4)
# img5 = cv2.rotate(image_bw,cv2.ROTATE_180  )

cv2.imshow("Before Histogram Equilized",image_bw)

cv2.imshow("Histogram Equilized",hist_eq)

# # cv2.imshow("Histogram Equilized Red",hist_eq2)
# # cv2.imshow("Histogram Equilized Green",hist_eq3)
# # cv2.imshow("Histogram Equilized Blue",hist_eq4)
# cv2.imshow('After rotating',img5)

histr = cv2.calcHist([image_bw], [0], None, [256], [0, 256])

plt.plot(histr)
plt.show()


cv2.waitKey(0)


