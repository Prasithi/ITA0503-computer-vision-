
import shutil
from pathlib import Path

import cv2
import pytesseract

from vision_utils import OUTPUT_DIR, resolve_input_path


# --------------------------------------------------
# 1. LOCATE TESSERACT OCR
# --------------------------------------------------

tesseract_path = Path(
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

if not tesseract_path.is_file():
    detected_path = shutil.which("tesseract")

    if detected_path:
        tesseract_path = Path(detected_path)
    else:
        raise FileNotFoundError(
            "Tesseract OCR not found. Install Tesseract first."
        )

pytesseract.pytesseract.tesseract_cmd = str(tesseract_path)


# --------------------------------------------------
# 2. IMAGE PREPROCESSING
# --------------------------------------------------

def preprocess_frame(frame):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Reduce noise while preserving edges
    enhanced = cv2.GaussianBlur(
        enhanced,
        (3, 3),
        0
    )

    return enhanced


# --------------------------------------------------
# 3. EXTRACT TEXT FROM VIDEO
# --------------------------------------------------

def extract_text_from_video(video_path):

    video_file = resolve_input_path(video_path)

    capture = cv2.VideoCapture(str(video_file))

    if not capture.isOpened():
        raise OSError(
            f"Cannot open video: {video_file}"
        )

    fps = capture.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    total_frames = int(
        capture.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    # Process one frame every second
    frame_interval = max(1, int(fps))

    extracted = []
    frame_count = 0
    processed_count = 0

    print("Starting video OCR...", flush=True)

    try:

        while True:

            ret, frame = capture.read()

            if not ret:
                break

            current_frame = frame_count
            frame_count += 1

            # Skip unnecessary frames
            if current_frame % frame_interval != 0:
                continue

            # Resize large frames
            height, width = frame.shape[:2]

            if width > 1280:

                new_height = int(
                    height * 1280 / width
                )

                frame = cv2.resize(
                    frame,
                    (1280, new_height),
                    interpolation=cv2.INTER_AREA
                )

            # Enhance image
            processed_frame = preprocess_frame(frame)

            try:

                text = pytesseract.image_to_string(
                    processed_frame,
                    config="--oem 3 --psm 11",
                    timeout=15
                )

                # Remove empty and very short lines
                lines = [
                    line.strip()
                    for line in text.splitlines()
                    if len(line.strip()) >= 3
                ]

                text = "\n".join(lines)

                if text.strip():

                    extracted.append(
                        f"Frame {current_frame}:\n{text}"
                    )

            except RuntimeError:

                print(
                    f"OCR timeout at frame {current_frame}",
                    flush=True
                )

            processed_count += 1

            print(
                f"Processed {processed_count} samples"
                f" | Video frame {frame_count}/{total_frames}",
                flush=True
            )

    finally:

        capture.release()
        cv2.destroyAllWindows()

    # --------------------------------------------------
    # 4. SAVE OCR RESULTS
    # --------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = OUTPUT_DIR / "ocr_results.txt"

    output_path.write_text(
        "\n\n".join(extracted),
        encoding="utf-8"
    )

    print("\nOCR processing completed.")

    print("Frames scanned:", frame_count)
    print("Frames sampled:", processed_count)
    print("Text sections found:", len(extracted))
    print("Results saved:", output_path)


# --------------------------------------------------
# 5. MAIN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    extract_text_from_video("input_video.mp4")
