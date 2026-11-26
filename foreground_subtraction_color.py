from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image

import cv2
import numpy as np

def subtract_foreground(image_path, lower_color, upper_color):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )

    lower_bound = np.array(
        lower_color,
        dtype=np.uint8
    )

    upper_bound = np.array(
        upper_color,
        dtype=np.uint8
    )

    mask = cv2.inRange(
        hsv,
        lower_bound,
        upper_bound
    )

    background = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    display_image("Original Image", image)

    display_image(
        "Foreground Subtracted Image",
        background
    )

    save_image("foreground_subtracted.jpg", background)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "sample.jpg"

lower_color = [0, 50, 50]
upper_color = [120, 255, 255]

subtract_foreground(
    image_path,
    lower_color,
    upper_color
)