
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(gray_image, kernel, iterations=1)

# Resize images for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display images
cv2.imshow("Original Grayscale Image", resize_for_display(gray_image))
cv2.imshow("Dilated Image", resize_for_display(dilated_image))

# Save output
cv2.imwrite("dilated_image_20.jpg", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image Dilation completed successfully!")
