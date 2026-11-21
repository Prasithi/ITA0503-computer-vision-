
import cv2
import numpy as np

def create_rectangle():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw rectangle
    cv2.rectangle(
        image,
        (width // 4, height // 4),
        (3 * width // 4, 3 * height // 4),
        (0, 0, 255),
        3
    )

    # Display image
    cv2.imshow("Rectangle Shape", image)

    # Save output
    cv2.imwrite("rectangle.jpg", image)

    print("Rectangle created successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


create_rectangle()
