
import cv2

# Read the input image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Resize to a bigger size (2x scaling)
bigger_image = cv2.resize(
    image, None,
    fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Resize to a smaller size (0.5x scaling)
smaller_image = cv2.resize(
    image, None,
    fx=0.5, fy=0.5,
    interpolation=cv2.INTER_AREA
)

# Resize copies for display only
def resize_for_display(img):
    height, width = img.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)
    return cv2.resize(
        img,
        (int(width * scale), int(height * scale)),
        interpolation=cv2.INTER_AREA
    )

# Display images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow("Bigger Image", resize_for_display(bigger_image))
cv2.imshow("Smaller Image", resize_for_display(smaller_image))

# Save resized images
cv2.imwrite("bigger_image.jpg", bigger_image)
cv2.imwrite("smaller_image.jpg", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image scaling completed successfully!")
