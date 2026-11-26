from pathlib import Path
import tempfile

import cv2


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "outputs"
MAX_DISPLAY_WIDTH = 800
MAX_DISPLAY_HEIGHT = 600
MAX_IMAGE_PIXELS = 25_000_000


def resolve_input_path(path):
    resolved = Path(path)
    if not resolved.is_absolute():
        resolved = PROJECT_DIR / resolved
    if not resolved.is_file():
        raise FileNotFoundError(f"Required input file not found: {resolved}")
    return resolved


def resolve_output_path(path):
    output = Path(path)
    if not output.is_absolute():
        output = OUTPUT_DIR / output
    elif output.parent == PROJECT_DIR:
        output = OUTPUT_DIR / output.name
    output.parent.mkdir(parents=True, exist_ok=True)
    return output


def display_image(window_name, image):
    if image is None or image.size == 0:
        raise ValueError(f"Cannot display an empty image: {window_name}")

    height, width = image.shape[:2]
    scale = min(
        MAX_DISPLAY_WIDTH / width,
        MAX_DISPLAY_HEIGHT / height,
        1.0,
    )
    if scale < 1.0:
        image = cv2.resize(
            image,
            (max(1, round(width * scale)), max(1, round(height * scale))),
            interpolation=cv2.INTER_AREA,
        )
    cv2.imshow(window_name, image)


def save_image(path, image):
    output = resolve_output_path(path)
    if not cv2.imwrite(str(output), image):
        raise OSError(f"Could not save image: {output}")
    return output


def load_cascade(filename):
    cascade_path = Path(cv2.data.haarcascades) / filename
    if not cascade_path.is_file():
        raise FileNotFoundError(f"OpenCV cascade file not found: {cascade_path}")
    cascade = cv2.CascadeClassifier(str(cascade_path))
    if cascade.empty():
        raise OSError(f"OpenCV could not load cascade file: {cascade_path}")
    return cascade


def read_image_dimensions():
    try:
        width = int(input("Enter image width: "))
        height = int(input("Enter image height: "))
    except ValueError as error:
        raise ValueError("Image width and height must be whole numbers.") from error

    if width <= 0 or height <= 0:
        raise ValueError("Image width and height must be greater than zero.")
    if width * height > MAX_IMAGE_PIXELS:
        raise ValueError(
            f"Requested image exceeds the {MAX_IMAGE_PIXELS:,}-pixel safety limit."
        )
    return width, height


def write_reversed_video(
    input_path,
    output_path,
    slow_factor=1.0,
    preview=False,
    window_name="Reversed Video",
):
    if slow_factor < 1:
        raise ValueError("slow_factor must be at least 1.")

    input_file = resolve_input_path(input_path)
    output_file = resolve_output_path(output_path)
    capture = cv2.VideoCapture(str(input_file))
    if not capture.isOpened():
        raise OSError(f"Could not open input video: {input_file}")

    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        capture.release()
        raise ValueError(f"Input video has an invalid frame rate: {input_file}")
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    try:
        with tempfile.TemporaryDirectory(prefix="cv_reverse_") as temporary_folder:
            frame_paths = []
            while True:
                ok, frame = capture.read()
                if not ok:
                    break
                frame_path = Path(temporary_folder) / f"{len(frame_paths):08d}.jpg"
                if not cv2.imwrite(
                    str(frame_path),
                    frame,
                    [cv2.IMWRITE_JPEG_QUALITY, 95],
                ):
                    raise OSError(f"Could not spool video frame: {frame_path}")
                frame_paths.append(frame_path)
            capture.release()

            if not frame_paths:
                raise ValueError(f"Input video contains no frames: {input_file}")

            output_fps = fps / slow_factor
            writer = cv2.VideoWriter(
                str(output_file),
                cv2.VideoWriter_fourcc(*"mp4v"),
                output_fps,
                (width, height),
            )
            if not writer.isOpened():
                writer.release()
                raise OSError(f"Could not create output video: {output_file}")

            display_preview = preview
            try:
                for frame_path in reversed(frame_paths):
                    frame = cv2.imread(str(frame_path))
                    if frame is None:
                        raise OSError(
                            f"Could not reload spooled frame: {frame_path}"
                        )
                    writer.write(frame)
                    if display_preview:
                        display_image(window_name, frame)
                        delay = max(1, round(1000 / output_fps))
                        if cv2.waitKey(delay) & 0xFF == ord("q"):
                            display_preview = False
            finally:
                writer.release()
                if preview:
                    cv2.destroyAllWindows()
    finally:
        capture.release()

    print(
        f"Reversed video saved: {output_file} "
        f"({width}x{height}, {len(frame_paths)} frames, {output_fps:g} fps)"
    )
    return output_file
