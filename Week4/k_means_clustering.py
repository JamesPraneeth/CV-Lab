import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Resources/example.png')
image = cv2.resize(image,(1400,700))

pixels = image.reshape((-1, 3))

pixels = np.float32(pixels)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

num_clusters = 8

_, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)

segmented_image = centers[labels.flatten()]

segmented_image = segmented_image.reshape(image.shape)



cv2.imshow('original',image)
cv2.imshow('k-means',segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

































































# Display the original image and segmented image
# images = [image, segmented_image]
# titles = ['original image', 'k-means image']
# for i in range(len(images)):
#  plt.subplot(1,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#  plt.title(titles[i])
#  plt.xticks([]),plt.yticks([])
# plt.show()