
import cv2

def segment_image(image_path, threshold_value=127):

    # Read the input image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image not found!")
        return

    # Apply thresholding for segmentation
    _, segmented_image = cv2.threshold(
        image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # Display original and segmented images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)

    # Save output image
    cv2.imwrite("segmented_image.jpg", segmented_image)

    print("Image segmentation completed successfully!")
    print("Threshold value:", threshold_value)
    print("Output saved as: segmented_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Execute the function
segment_image(
    r"C:\Users\Dell\Desktop\Image_Processing\image.jpg",
    127
)
