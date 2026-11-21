
import cv2

def detect_faces(image_path):

    face_cascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    if face_cascade.empty():
        print("Error: Cascade file not loaded!")
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

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

    print("Number of faces detected:", len(faces))

    cv2.imwrite("face_detected.jpg", image)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_faces(r"C:\Users\Dell\Desktop\Image_Processing\image.jpg")
