
import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
rows, cols, ch = image.shape

# Define three points in the original image
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Define their corresponding transformed positions
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Calculate the Affine Transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the transformation
transformed_image = cv2.warpAffine(
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
    "Affine Transformed Image",
    resize_for_display(transformed_image)
)

# Save the transformed image
cv2.imwrite("affine_transformed.jpg", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Affine Transformation completed successfully!")

