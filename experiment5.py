
import matplotlib
matplotlib.use("Qt5Agg")

import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):

    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("ERROR: Image not found!")
        return

    print("Image loaded successfully!")

    # Convert BGR to RGB for Matplotlib
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create display area
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Display original image
    axes[0].imshow(rgb_image)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    # Define color channels
    colors = ('b', 'g', 'r')

    # Calculate and plot histograms
    for i, color in enumerate(colors):

        histogram = cv2.calcHist(
            [image], [i], None, [256], [0, 256]
        )

        axes[1].plot(
            histogram,
            color=color,
            label=color.upper() + " Channel"
        )

    axes[1].set_title("Color Histogram Analysis")
    axes[1].set_xlabel("Pixel Intensity")
    axes[1].set_ylabel("Frequency")
    axes[1].set_xlim([0, 256])
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()
    plt.show()


# Execute function
analyze_histogram("sample.jpg")
