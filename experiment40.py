import cv2
import pytesseract

def extract_text_from_video(video_path):

    # Set Tesseract executable path
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Video not found!")
        return

    print("Extracted Text from Video:")

    # Read video frames
    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        # Extract text using OCR
        text = pytesseract.image_to_string(gray_frame)

        if text.strip():
            print(text)

    cap.release()
    cv2.destroyAllWindows()


# Example usage
video_path = r"C:\Users\Dell\Desktop\Image_Processing\sample.mp4"

extract_text_from_video(video_path)
