import cv2
import matplotlib.pyplot as plt
from cv2 import SIFT_create
import numpy as np
img=cv2.imread('Resources/image2.jpeg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
sift=SIFT_create()
keypoints, descriptors=sift.detectAndCompute(img, None)
keypoints_with_size=np.copy(img)
cv2.drawKeypoints(img, keypoints, keypoints_with_size, color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Keypoints', keypoints_with_size)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(keypoints_with_size)
plt.show()