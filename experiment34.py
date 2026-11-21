
import cv2
import numpy as np

def create_circle():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate center and radius
    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    # Draw circle
    cv2.circle(
        image,
        center,
        radius,
        (255, 0, 0),
        3
    )

    # Display image
    cv2.imshow("Circle Shape", image)

    # Save output
    cv2.imwrite("circle.jpg", image)

    print("Circle created successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


create_circle()
