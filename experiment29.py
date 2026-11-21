
import cv2

def detect_eyes(image_path):

    # Load face and eye classifiers
    face_cascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    eye_cascade = cv2.CascadeClassifier(
        "haarcascade_eye.xml"
    )

    if face_cascade.empty() or eye_cascade.empty():
        print("Error: XML file not loaded!")
        return

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, 1.1, 5, minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        # Extract face region
        face_roi = gray[y:y+h, x:x+w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(15, 15)
        )

        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                image,
                (x + ex, y + ey),
                (x + ex + ew, y + ey + eh),
                (255, 0, 0),
                2
            )

    print("Number of faces detected:", len(faces))

    # Save output
    cv2.imwrite("eye_detected.jpg", image)

    # Display result
    cv2.imshow("Eye Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_eyes(
    r"C:\Users\Dell\Desktop\Image_Processing\image.jpg"
)
