import cv2
import numpy as np


image = cv2.imread('C:/Users/ugcse.PG-CP.000/Desktop/210962162/Week3/Resources/example.png', cv2.IMREAD_GRAYSCALE)


gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)


gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
gradient_direction = np.arctan2(gradient_y, gradient_x)

gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
