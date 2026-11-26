from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image

import cv2
import numpy as np

image = cv2.imread(str(resolve_input_path(r"sample.jpg")))

if image is None:
    raise FileNotFoundError("sample.jpg not found")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)

top_hat_image = cv2.morphologyEx(
    gray_image,
    cv2.MORPH_TOPHAT,
    kernel
)

display_image("Original Image", image)
display_image("Top Hat Image", top_hat_image)

save_image("top_hat_image.jpg", top_hat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()