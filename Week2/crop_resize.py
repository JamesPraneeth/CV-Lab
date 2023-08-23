import cv2
import matplotlib.pyplot as plt


image = cv2.imread('/Resources/pic1.jpg')

# Resize the image
new_width = 300
new_height = 200
resized_image = cv2.resize(image, (new_width, new_height))


crop_x = 50
crop_y = 30
crop_width = 150
crop_height = 100


cropped_image = resized_image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.axis('off')

plt.tight_layout()
plt.show()
