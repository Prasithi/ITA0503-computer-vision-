
import cv2

# Read original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Apply Gaussian Blur at original resolution
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Resize only for display
display_width = 600
display_height = 400

original_display = cv2.resize(
    image, (display_width, display_height)
)

blurred_display = cv2.resize(
    blurred_image, (display_width, display_height)
)

# Display images
cv2.imshow("Original Image", original_display)
cv2.imshow("Gaussian Blurred Image", blurred_display)

# Save full-resolution output
cv2.imwrite("blurred_output.jpg", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Gaussian Blur completed successfully!")
