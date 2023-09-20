import cv2
import numpy as np

image = cv2.imread("Resources/image2.jpeg")
image = cv2.resize(image,(0,0),fy=0.5,fx=0.5)
# print(image.shape)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()