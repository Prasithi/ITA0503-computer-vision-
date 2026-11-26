from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image


import cv2
import numpy as np

# Read the input image
image = cv2.imread(str(resolve_input_path(r"sample.jpg")))

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
display_image("Original Image", resize_for_display(image))
display_image(
    "Perspective Transformed Image",
    resize_for_display(transformed_image)
)

# Save the transformed image
save_image("perspective_transformed.jpg", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Perspective Transformation completed successfully!")

