
import cv2

# Read the original image
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define ROI coordinates
x1 = width // 4
y1 = height // 4
x2 = 3 * width // 4
y2 = 3 * height // 4

# Crop the selected region
roi = image[y1:y2, x1:x2]

# Copy the original image
output_image = image.copy()

# Paste the cropped region at another position
paste_x = 0
paste_y = 0

roi_height, roi_width = roi.shape[:2]

output_image[
    paste_y:paste_y + roi_height,
    paste_x:paste_x + roi_width
] = roi

# Draw a rectangle around the selected ROI
marked_image = image.copy()
cv2.rectangle(
    marked_image,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    2
)

# Resize images only for display
def resize_for_display(img):
    h, w = img.shape[:2]
    scale = min(800 / w, 600 / h, 1.0)
    return cv2.resize(
        img,
        (int(w * scale), int(h * scale))
    )

# Display the images
cv2.imshow("Original Image", resize_for_display(image))
cv2.imshow("Selected ROI", resize_for_display(roi))
cv2.imshow("Cropped and Pasted Image", resize_for_display(output_image))
cv2.imshow("ROI Selection", resize_for_display(marked_image))

# Save the output images
cv2.imwrite("cropped_roi.jpg", roi)
cv2.imwrite("roi_pasted.jpg", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image cropping, copying and pasting completed!")
