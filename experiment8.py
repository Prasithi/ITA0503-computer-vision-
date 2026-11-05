
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(gray_image, kernel, iterations=1)

# Resize images for display only
height, width = gray_image.shape
scale = min(800 / width, 600 / height, 1.0)

new_size = (int(width * scale), int(height * scale))

original_display = cv2.resize(gray_image, new_size)
dilated_display = cv2.resize(dilated_image, new_size)

# Display the images
cv2.imshow("Original Grayscale Image", original_display)
cv2.imshow("Dilated Image", dilated_display)

# Save the output
cv2.imwrite("dilated_output.jpg", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image dilation completed successfully!")
