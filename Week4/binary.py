import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/Resources/example.png',0)
img = cv.resize(img,(1400,700))

# cv.imshow('image',image)
ret,thresh1 = cv.threshold(img,130,255,cv.THRESH_BINARY)
print(ret)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
print(ret)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
print(ret)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
print(ret)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
print(ret)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
 plt.subplot(3,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
 plt.title(titles[i])
 plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

# import cv2
# import numpy as np
#
# # Load an image in grayscale
# image = cv2.imread('/Resources/example.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.resize(image,(1400,700))
#
# # Apply thresholding using a fixed threshold value
# _, binary_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#
# # Apply adaptive thresholding
# adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                           cv2.THRESH_BINARY, 11, 2)
#
# # Display the original, binary threshold, and adaptive threshold images
# cv2.imshow('Original Image', image)
# # cv2.imshow('Binary Threshold', binary_threshold)
# cv2.imshow('Adaptive Threshold', adaptive_threshold)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
