from vision_utils import (
    display_image,
    load_cascade,
    resolve_input_path,
    save_image,
)

import cv2

def detect_faces(image_path):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    face_cascade = load_cascade("haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    print("Faces detected:", len(faces))

    display_image("Face Detection", image)
    save_image("face_detection.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_faces("sample.jpg")