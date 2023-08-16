import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/ugcse.PG-CP.000/Desktop/210962162/Week3/Resources/example.png', cv2.IMREAD_GRAYSCALE)

# Calculate gradients using Sobel operators
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate magnitude and direction of gradient
gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
gradient_direction = np.arctan2(gradient_y, gradient_x)

# Convert gradient magnitude to uint8 (0-255) for visualization
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Display the original image and gradient magnitude
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
