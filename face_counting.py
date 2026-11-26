from vision_utils import (
    display_image,
    load_cascade,
    resolve_input_path,
    save_image,
)

import cv2

def count_faces(image_path):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    face_cascade = load_cascade("haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    face_count = len(faces)

    print("Number of faces detected:", face_count)

    for (x, y, w, h) in faces:

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.putText(
        image,
        f"Faces: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    display_image("Face Counting", image)

    save_image("face_count_result.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_count


count_faces("sample.jpg")