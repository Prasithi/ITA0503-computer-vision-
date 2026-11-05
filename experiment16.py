
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator in X direction
sobel_x = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

# Apply Sobel operator in Y direction
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

# Convert results to absolute 8-bit images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y gradients
sobel_output = cv2.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)

# Resize images only for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow("Sobel X", resize_for_display(sobel_x))
cv2.imshow("Sobel Y", resize_for_display(sobel_y))
cv2.imshow("Sobel Edge Detection", resize_for_display(sobel_output))

# Save the output
cv2.imwrite("sobel_output.jpg", sobel_output)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Sobel Edge Detection completed successfully!")
