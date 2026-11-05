
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(
    gray,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Dilate corner points for better visibility
harris_corners = cv2.dilate(
    harris_corners,
    None
)

# Mark detected corners in red
output_image = image.copy()
output_image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

# Resize images only for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display original and corner-detected images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow("Harris Corner Detection", resize_for_display(output_image))

# Save the output image
cv2.imwrite("harris_corners.jpg", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Harris Corner Detection completed successfully!")

