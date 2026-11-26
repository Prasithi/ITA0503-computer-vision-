from vision_utils import (
    display_image,
    load_cascade,
    resolve_input_path,
    save_image,
)

import cv2

def detect_smile(image_path):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    face_cascade = load_cascade("haarcascade_frontalface_default.xml")
    smile_cascade = load_cascade("haarcascade_smile.xml")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        5,
        minSize=(30, 30)
    )

    smile_count = 0
    for (x, y, w, h) in faces:

        face_roi = gray[y:y+h, x:x+w]

        smile_roi = face_roi[h//2:, :]

        smiles = smile_cascade.detectMultiScale(
            smile_roi,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )
        smile_count += len(smiles)

        for (sx, sy, sw, sh) in smiles:

            cv2.rectangle(
                image,
                (x + sx, y + h//2 + sy),
                (x + sx + sw, y + h//2 + sy + sh),
                (0, 255, 0),
                2
            )

    print("Smiles detected:", smile_count)
    display_image("Smile Detection", image)
    save_image("smile_detection.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_smile("sample.jpg")