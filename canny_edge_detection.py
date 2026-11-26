from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image


import cv2

# Read the original image
image = cv2.imread(str(resolve_input_path(r"sample.jpg")))

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Set maximum display dimensions
max_width = 800
max_height = 600

# Calculate display size while preserving aspect ratio
height, width = image.shape[:2]
scale = min(max_width / width, max_height / height, 1.0)

new_width = int(width * scale)
new_height = int(height * scale)

# Resize images for display only
original_display = cv2.resize(
    image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

edges_display = cv2.resize(
    edges, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

# Display images
display_image("Original Image", original_display)
display_image("Canny Edge Detection", edges_display)

# Save full-resolution edge image
save_image("canny_output.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canny Edge Detection completed successfully!")
