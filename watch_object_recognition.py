
from pathlib import Path
import cv2
import numpy as np

from vision_utils import PROJECT_DIR, display_image, save_image

# 1. Load input image
image_path = PROJECT_DIR / "watch.jpg"
image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(f"Cannot read image: {image_path}")

# Keep original image unchanged
result = image.copy()

# 2. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 2)

# 3. Detect circular watch dial
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=100,
    param2=45,
    minRadius=50,
    maxRadius=0
)

if circles is None:
    print("No circular watch dial detected.")
else:
    circles = np.round(circles[0]).astype(int)

    # Select the largest detected circle
    x, y, radius = max(circles, key=lambda c: c[2])

    # 4. Estimate the complete watch area, including strap
    x1 = max(0, x - int(radius * 1.25))
    y1 = max(0, y - int(radius * 1.95))
    x2 = min(image.shape[1], x + int(radius * 1.25))
    y2 = min(image.shape[0], y + int(radius * 1.95))

    # 5. Draw bounding box and dial circle
    cv2.rectangle(result, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.circle(result, (x, y), radius, (255, 0, 0), 2)

    cv2.putText(
        result,
        "Possible Watch",
        (x1, max(y1 - 10, 25)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    print("Possible watch dial detected.")
    print("Estimated watch bounding box:", (x1, y1, x2, y2))

# 6. Display and save result
display_image("Watch Detection", result)
save_image("watch_detection.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
