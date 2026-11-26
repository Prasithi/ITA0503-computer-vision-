from vision_utils import display_image, read_image_dimensions, save_image

import numpy as np
import cv2

def create_rectangle_image(image_size):

    height, width = image_size

    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    top_left = (width // 4, height // 4)

    bottom_right = (
        3 * width // 4,
        3 * height // 4
    )

    cv2.rectangle(
        image,
        top_left,
        bottom_right,
        (255, 0, 0),
        2
    )

    display_image("Rectangle Image", image)

    save_image("rectangle_image.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


user_width, user_height = read_image_dimensions()
create_rectangle_image((user_height, user_width))