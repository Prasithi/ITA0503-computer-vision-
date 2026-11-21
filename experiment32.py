
import cv2
import numpy as np

def create_colored_boxes():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate box size
    box_h = height // 10
    box_w = width // 10

    # Draw four colored boxes
    image[0:box_h, 0:box_w] = (0, 0, 0)       # Black
    image[0:box_h, width-box_w:width] = (255, 0, 0)  # Blue
    image[height-box_h:height, 0:box_w] = (0, 255, 0) # Green
    image[height-box_h:height, width-box_w:width] = (0, 0, 255) # Red

    # Display image
    cv2.imshow("Four Colored Boxes", image)

    # Save output
    cv2.imwrite("colored_boxes.jpg", image)

    print("Four colored boxes created successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


create_colored_boxes()
