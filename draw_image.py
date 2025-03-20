import pytesseract
from PIL import Image, ImageDraw


def draw_image(image_path):
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    print(text)

    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    draw = ImageDraw.Draw(image)
    for i, word in enumerate(data["text"]):
        if word.find("...") != -1:
            print(f"Found ellipsis on word: {word} at index: {i}")

            x, y, w, h = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

    image.show()
