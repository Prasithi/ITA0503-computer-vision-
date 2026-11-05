
import cv2

# Read the original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

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

equalized_display = cv2.resize(
    equalized_image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

# Display images
cv2.imshow("Original Grayscale Image", original_display)
cv2.imshow("Histogram Equalized Image", equalized_display)

# Save full-resolution output
cv2.imwrite("equalized_output.jpg", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Histogram Equalization completed successfully!")
