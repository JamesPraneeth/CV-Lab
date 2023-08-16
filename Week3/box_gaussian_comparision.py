import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('C:/Users/ugcse.PG-CP.000/Desktop/210962162/Week3/Resources/example.png',0)

# Apply box filter
box_filtered = cv2.boxFilter(image, -1, (5, 5))

# Apply Gaussian filter
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)

# Display original, box filtered, and Gaussian filtered images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(box_filtered, cv2.COLOR_BGR2RGB))
plt.title('Box Filtered Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(gaussian_filtered, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
