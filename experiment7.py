
import cv2

# Open the video
cap = cv2.VideoCapture("input_video.mp4")

if not cap.isOpened():
    print("Error: Video file not found!")
    exit()

# Read video properties
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

normal_delay = int(1000 / fps)

print("Press 1 for Normal Speed")
print("Press 2 for Slow Motion")
print("Press 3 for Fast Motion")
print("Press Q to Exit")

speed = normal_delay

while True:
    ret, frame = cap.read()

    if not ret:
        # Restart video after reaching the end
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize only for display
    height, width = frame.shape[:2]
    scale = min(800 / width, 600 / height, 1.0)

    display_frame = cv2.resize(
        frame,
        (int(width * scale), int(height * scale))
    )

    cv2.imshow("Video Processing", display_frame)

    key = cv2.waitKey(speed) & 0xFF

    if key == ord('1'):
        speed = normal_delay
        print("Normal Speed")

    elif key == ord('2'):
        speed = normal_delay * 3
        print("Slow Motion")

    elif key == ord('3'):
        speed = max(1, normal_delay // 3)
        print("Fast Motion")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Video processing completed!")
