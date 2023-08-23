import cv2
import numpy as np
image = cv2.imread("/Resources/example.png",1)


img2 = cv2.resize(image,(500,500))

gaussian_3 = cv2.GaussianBlur(img2, (0, 0), 2.0)

unsharp_image = cv2.addWeighted(img2, 2, gaussian_3, -2,0)

result2 = np.hstack((img2,unsharp_image))

cv2.imshow("result2", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
