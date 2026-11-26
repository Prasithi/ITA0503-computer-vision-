from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image


import cv2

# Read original image
image = cv2.imread(str(resolve_input_path(r"sample.jpg")))

if image is None:
    print("Image not found!")
    exit()

# Apply Gaussian Blur at original resolution
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display images
display_image("Original Image", image)
display_image("Gaussian Blurred Image", blurred_image)

# Save full-resolution output
save_image("blurred_output.jpg", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Gaussian Blur completed successfully!")
