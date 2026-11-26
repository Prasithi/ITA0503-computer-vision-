
from pathlib import Path
import cv2
from ultralytics import YOLO

from vision_utils import OUTPUT_DIR, resolve_input_path

# Set True to display live video; False for automated testing
SHOW_PREVIEW = False

VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck",
}


def detect_vehicles(video_path):
    video_file = resolve_input_path(video_path)

    if not video_file.is_file():
        raise FileNotFoundError(f"Video not found: {video_file}")

    # Downloads pretrained model automatically on first run
    model = YOLO("yolov8n.pt")

    capture = cv2.VideoCapture(str(video_file))

    if not capture.isOpened():
        raise OSError(f"Cannot open video: {video_file}")

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25.0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "vehicle_detection.mp4"

    writer = cv2.VideoWriter(
        str(output_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )

    if not writer.isOpened():
        capture.release()
        raise OSError("Could not create output video.")

    frame_count = 0
    vehicle_count = 0

    try:
        while True:
            ret, frame = capture.read()

            if not ret:
                break

            results = model.predict(
                frame,
                conf=0.35,
                verbose=False
            )

            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])

                    if class_id not in VEHICLE_CLASSES:
                        continue

                    x1, y1, x2, y2 = map(
                        int, box.xyxy[0].tolist()
                    )

                    label = VEHICLE_CLASSES[class_id]
                    confidence = float(box.conf[0])

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    cv2.putText(
                        frame,
                        f"{label}: {confidence:.2f}",
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

                    vehicle_count += 1

            writer.write(frame)
            frame_count += 1

            if SHOW_PREVIEW:
                cv2.imshow("Vehicle Detection", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    finally:
        capture.release()
        writer.release()
        cv2.destroyAllWindows()

    print("Frames processed:", frame_count)
    print("Vehicle detections:", vehicle_count)
    print("Output saved:", output_path)


if __name__ == "__main__":
    detect_vehicles("input_video.mp4")
