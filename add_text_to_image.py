from vision_utils import PROJECT_DIR, display_image, resolve_input_path, save_image

import cv2

def add_text_to_image(image_path, text):

    image = cv2.imread(str(resolve_input_path(image_path)))

    if image is None:
        raise FileNotFoundError(image_path)

    if not text.strip():
        raise ValueError("Text to render must not be empty.")

    height, width = image.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX

    font_scale = 1.0
    font_thickness = 2

    text_color = (0, 0, 255)

    text_size = cv2.getTextSize(
        text,
        font,
        font_scale,
        font_thickness
    )[0]
    if text_size[0] > width - 40:
        font_scale *= max(0.1, (width - 40) / text_size[0])
        text_size = cv2.getTextSize(
            text,
            font,
            font_scale,
            font_thickness
        )[0]

    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    cv2.putText(
        image,
        text,
        (text_x, text_y),
        font,
        font_scale,
        text_color,
        font_thickness
    )

    display_image("Image with Text", image)

    save_image("image_with_text.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


user_text = input("Enter the text to display: ")

add_text_to_image("sample.jpg", user_text)