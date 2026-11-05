
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
rows, cols, ch = image.shape

# Define four points in the original image
pts1 = np.float32([
    [50, 50],
    [400, 50],
    [50, 400],
    [400, 400]
])

# Define four corresponding destination points
pts2 = np.float32([
    [10, 100],
    [300, 50],
    [100, 300],
    [350, 350]
])

# Calculate the Perspective Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
transformed_image = cv2.warpPerspective(
    image, matrix, (cols, rows)
)

# Resize images only for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display original and transformed images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow(
    "Perspective Transformed Image",
    resize_for_display(transformed_image)
)

# Save the transformed image
cv2.imwrite("perspective_transformed.jpg", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Perspective Transformation completed successfully!")

