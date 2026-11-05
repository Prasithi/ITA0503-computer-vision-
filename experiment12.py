
import cv2

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Rotate the flipped image by 90 degrees counterclockwise
rotated_image = cv2.rotate(
    flipped_image,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)

# Resize images only for display
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale))
    )

# Display the images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow(
    "Rotated 270 Degree Image",
    resize_for_display(rotated_image)
)

# Save the output image
cv2.imwrite("rotated_image_270.jpg", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Experiment 12 completed successfully!")

