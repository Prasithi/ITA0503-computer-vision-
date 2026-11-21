import cv2

def count_faces(image_path):

    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade model
    face_cascade = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    if face_cascade.empty():
        print("Error: Face cascade file not found!")
        return

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count faces
    face_count = len(faces)
    print("Number of faces detected:", face_count)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display the image
    cv2.imshow("Face Detection", image)
    cv2.imwrite("face_count_result.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_count


# Example usage
image_path = r"C:\Users\Dell\Desktop\Image_Processing\image.jpg"

count_faces(image_path)
