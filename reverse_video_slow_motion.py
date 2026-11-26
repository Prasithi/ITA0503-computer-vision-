from vision_utils import write_reversed_video


if __name__ == "__main__":
    write_reversed_video(
        "input_video.mp4",
        "output_reversed_slow.mp4",
        slow_factor=4,
        preview=True,
        window_name="Reverse Slow Motion Video",
    )