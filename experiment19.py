
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
eroded_image = cv2.erode(
    gray_image,
    kernel,
    iterations=1
)

# Resize images only for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display original and eroded images
cv2.imshow("Original Grayscale Image", resize_for_display(gray_image))
cv2.imshow("Eroded Image", resize_for_display(eroded_image))

# Save the output
cv2.imwrite("eroded_image_19.jpg", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image Erosion completed successfully!")
