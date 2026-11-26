from vision_utils import display_image, read_image_dimensions, save_image

import numpy as np
import cv2

def create_colored_corners(image_size):

    height, width = image_size

    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    box_h = height // 10
    box_w = width // 10

    # Top-left: Black
    image[:box_h, :box_w] = [0, 0, 0]

    # Top-right: Blue
    image[:box_h, -box_w:] = [255, 0, 0]

    # Bottom-left: Green
    image[-box_h:, :box_w] = [0, 255, 0]

    # Bottom-right: Red
    image[-box_h:, -box_w:] = [0, 0, 255]

    display_image("Colored Corners Image", image)

    save_image("colored_corners.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


user_width, user_height = read_image_dimensions()
create_colored_corners((user_height, user_width))