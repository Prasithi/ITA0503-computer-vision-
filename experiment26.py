
import cv2

def reverse_video(input_video_path, output_video_path):

    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25.0

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        fps,
        (frame_width, frame_height)
    )

    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        out.release()
        print("Error: No frames found")
        return

    # Reverse frames
    frames.reverse()

    # Write frames in reverse order
    for frame in frames:
        out.write(frame)

    out.release()

    print("Video reversed successfully!")
    print("Total frames:", len(frames))
    print("Reversed video saved as:", output_video_path)


# Example usage
reverse_video("sample.mp4", "output_reversed.mp4")
