
import cv2

# Read the original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Copy the original image
watermarked_image = image.copy()

# Define watermark text
watermark_text = "COPYRIGHT"

# Get image dimensions
height, width = image.shape[:2]

# Set watermark position
position = (width - 220, height - 30)

# Insert watermark text
cv2.putText(
    watermarked_image,
    watermark_text,
    position,
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# Resize images only for display
def resize_for_display(img):
    h, w = img.shape[:2]
    scale = min(800 / w, 600 / h, 1.0)
    return cv2.resize(
        img,
        (int(w * scale), int(h * scale))
    )

# Display original and watermarked images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow(
    "Watermarked Image",
    resize_for_display(watermarked_image)
)

# Save watermarked image
cv2.imwrite("watermarked_image.jpg", watermarked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Watermark added successfully!")

