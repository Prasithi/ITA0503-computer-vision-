import cv2

# Read the original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set maximum display dimensions
max_width = 800
max_height = 600

# Calculate resizing scale while preserving aspect ratio
height, width = image.shape[:2]
scale = min(max_width / width, max_height / height, 1.0)

new_width = int(width * scale)
new_height = int(height * scale)

# Resize only for display
original_display = cv2.resize(
    image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

gray_display = cv2.resize(
    gray_image, (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

# Display images
cv2.imshow("Original Image", original_display)
cv2.imshow("Grayscale Image", gray_display)

# Save full-resolution grayscale image
cv2.imwrite("grayscale_output.jpg", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Grayscale conversion completed successfully!")