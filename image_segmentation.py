from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image

import cv2

def segment_image(image_path, threshold_value=127):

    image = cv2.imread(
        str(resolve_input_path(image_path)),
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        raise FileNotFoundError(image_path)

    _, segmented_image = cv2.threshold(
        image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    display_image("Original Image", image)
    display_image("Segmented Image", segmented_image)

    save_image("segmented_image.jpg", segmented_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


segment_image("sample.jpg", 127)