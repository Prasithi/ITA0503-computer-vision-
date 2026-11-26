from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image

import cv2
import numpy as np

image = cv2.imread(str(resolve_input_path(r"sample.jpg")), cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("sample.jpg not found")

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5, 5)
)

blackhat = cv2.morphologyEx(
    image,
    cv2.MORPH_BLACKHAT,
    kernel
)

display_image("Original Image", image)
display_image("Black Hat Image", blackhat)

save_image("blackhat_image.jpg", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()