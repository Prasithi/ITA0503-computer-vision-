
import cv2

def detect_smile(image_path):

    # Load face and smile classifiers
    face_cascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    smile_cascade = cv2.CascadeClassifier(
        "haarcascade_smile.xml"
    )

    if face_cascade.empty() or smile_cascade.empty():
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

    smile_count = 0

    for (x, y, w, h) in faces:

        # Extract lower half of face
        face_roi = gray[y + h//2:y + h, x:x + w]

        # Detect smiles
        smiles = smile_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )

        smile_count += len(smiles)

        # Draw rectangles around smiles
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                image,
                (x + sx, y + h//2 + sy),
                (x + sx + sw, y + h//2 + sy + sh),
                (0, 255, 0),
                2
            )

    print("Number of faces detected:", len(faces))
    print("Number of smiles detected:", smile_count)

    # Save output
    cv2.imwrite("smile_detected.jpg", image)

    # Display result
    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_smile(
    r"C:\Users\Dell\Desktop\Image_Processing\image.jpg"
)
