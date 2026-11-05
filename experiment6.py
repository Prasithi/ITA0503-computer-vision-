
import cv2
import numpy as np

# Read the original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(gray_image, kernel, iterations=1)

# Set maximum display dimensions
max_width = 800
max_height = 600

# Calculate display size while preserving aspect ratio
height, width = gray_image.shape[:2]
scale = min(max_width / width, max_height / height, 1.0)

new_width = int(width * scale)
new_height = int(height * scale)

# Resize images for display only
original_display = cv2.resize(
    gray_image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

eroded_display = cv2.resize(
    eroded_image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

# Display images
cv2.imshow("Original Grayscale Image", original_display)
cv2.imshow("Eroded Image", eroded_display)

# Save full-resolution output
cv2.imwrite("eroded_output.jpg", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image Erosion completed successfully!")
