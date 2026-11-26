from vision_utils import display_image, resolve_input_path, save_image

import cv2
import numpy as np

# Load the input image from the project folder
image_path = resolve_input_path("sample.jpg")
image = cv2.imread(str(image_path))

# Check whether image loaded successfully
if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply morphological opening
opened_image = cv2.morphologyEx(
    gray_image,
    cv2.MORPH_OPEN,
    kernel
)

# Display images
display_image("Original Image", image)
display_image("Opened Image", opened_image)

# Save the output image in the outputs folder
output_path = save_image("opened_image.jpg", opened_image)

print(f"Output saved successfully: {output_path}")

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
