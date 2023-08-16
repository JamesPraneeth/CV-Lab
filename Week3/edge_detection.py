import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('C:/Users/ugcse.PG-CP.000/Desktop/210962162/Week3/Resources/example.png', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the magnitude of the gradient
gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

# Normalize the gradient magnitude to the range [0, 255]
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Display the original image and edges detected
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Edges Detected (Sobel)')
plt.axis('off')

plt.tight_layout()
plt.show()
