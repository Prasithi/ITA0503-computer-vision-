import matplotlib

matplotlib.use("Agg")

import cv2
import matplotlib.pyplot as plt

from vision_utils import OUTPUT_DIR, display_image, resolve_input_path


def analyze_histogram(image_path):
    image_path = resolve_input_path(image_path)
    image = cv2.imread(str(image_path))
    if image is None:
        raise OSError(f"Could not read image: {image_path}")

    print("Image loaded successfully!")
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].imshow(rgb_image)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    for channel, color in enumerate(("b", "g", "r")):
        histogram = cv2.calcHist([image], [channel], None, [256], [0, 256])
        axes[1].plot(
            histogram,
            color=color,
            label=f"{color.upper()} Channel",
        )

    axes[1].set_title("Color Histogram Analysis")
    axes[1].set_xlabel("Pixel Intensity")
    axes[1].set_ylabel("Frequency")
    axes[1].set_xlim([0, 256])
    axes[1].legend()
    axes[1].grid()
    fig.tight_layout()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plot_path = OUTPUT_DIR / "histogram_output.png"
    fig.savefig(plot_path)
    plt.close(fig)

    histogram_image = cv2.imread(str(plot_path))
    if histogram_image is None:
        raise OSError(f"Could not reload generated histogram: {plot_path}")
    display_image("Color Histogram Analysis", histogram_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"Histogram saved: {plot_path}")


if __name__ == "__main__":
    analyze_histogram("sample.jpg")
