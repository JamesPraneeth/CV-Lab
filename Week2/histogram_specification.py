import cv2
import numpy as np
import matplotlib.pyplot as plt


input_image = cv2.imread('/Resources/pic1.jpg', cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread('/Resources/example.png', cv2.IMREAD_GRAYSCALE)

if input_image is None or reference_image is None:
    print("Error loading images.")
else:

    input_hist, _ = np.histogram(input_image.flatten(), bins=256, range=[0,256])
    reference_hist, _ = np.histogram(reference_image.flatten(), bins=256, range=[0,256])


    input_cumulative_hist = input_hist.cumsum()
    reference_cumulative_hist = reference_hist.cumsum()


    input_cumulative_hist = (input_cumulative_hist / input_cumulative_hist[-1]) * 255
    reference_cumulative_hist = (reference_cumulative_hist / reference_cumulative_hist[-1]) * 255


    output_image = np.interp(input_image.flatten(), input_cumulative_hist, reference_cumulative_hist)
    output_image = output_image.reshape(input_image.shape).astype(np.uint8)


    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(reference_image, cmap='gray')
    plt.title('Reference Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(output_image, cmap='gray')
    plt.title('Histogram Specified Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
