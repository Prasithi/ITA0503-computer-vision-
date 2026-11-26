from vision_utils import (
    display_image,
    load_cascade,
    resolve_input_path,
    save_image,
)

import cv2

def detect_eyes(image_path):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    face_cascade = load_cascade("haarcascade_frontalface_default.xml")
    eye_cascade = load_cascade("haarcascade_eye.xml")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        5,
        minSize=(30, 30)
    )

    eye_count = 0
    for (x, y, w, h) in faces:

        face_roi = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_roi,
            1.1,
            10,
            minSize=(15, 15)
        )
        eye_count += len(eyes)

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                image,
                (x + ex, y + ey),
                (x + ex + ew, y + ey + eh),
                (255, 0, 0),
                2
            )

    print("Eyes detected:", eye_count)
    display_image("Eye Detection", image)
    save_image("eye_detection.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_eyes("sample.jpg")