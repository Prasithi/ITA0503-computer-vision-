from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image


import cv2

# Read the input image
image = cv2.imread(str(resolve_input_path(r"sample.jpg")))

if image is None:
    print("Image not found!")
    exit()

# Rotate the image 90 degrees clockwise
rotated_image = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE
)

# Resize images for display only
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)

    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display original and rotated images
display_image("Original Image", resize_for_display(image))
display_image("Rotated 90 Degree Clockwise",
           resize_for_display(rotated_image))

# Save the rotated image
save_image("rotated_image_90.jpg", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("90-degree clockwise rotation completed successfully!")
