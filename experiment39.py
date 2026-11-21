import cv2

def play_video_reverse_slow(video_path):

    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Video not found!")
        return

    frames = []

    # Extract all frames
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Total frames:", len(frames))
    print("Playing video in reverse slow motion...")

    # Play frames in reverse
    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Example usage
video_path = r"C:\Users\Dell\Desktop\Image_Processing\sample.mp4"

play_video_reverse_slow(video_path)
