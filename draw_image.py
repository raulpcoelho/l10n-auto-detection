import pytesseract
from PIL import Image, ImageDraw
import os


def draw_image(image_path, output_images_path, words_to_highlight):

    image = Image.open(image_path)

    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    highlighted = False
    for i, word in enumerate(data["text"]):
        if len(word) == 0:
            continue
        if word.find("...") != -1:
            highlighted = True
            draw = ImageDraw.Draw(image)
            print(f"Highlighting ellipsis on word: {word}")
            x, y, w, h = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            if word == "...":
                x -= 5
                w += 10
                y += 5
                h -= 10

            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

            os.makedirs(output_images_path, exist_ok=True)
            with open(
                f"{output_images_path}/words.txt", "a+", encoding="utf-8"
            ) as file:
                file.seek(0)
                existing_words = file.read().splitlines()
                if word + "(possível erro de elipse)" not in existing_words:
                    file.write(word + "(possível erro de elipse)" + "\n")
        if word in words_to_highlight:
            highlighted = True
            draw = ImageDraw.Draw(image)

            print(f"Highlighting word: {word}")

            x, y, w, h = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

            os.makedirs(output_images_path, exist_ok=True)
            with open(
                f"{output_images_path}/words.txt", "a+", encoding="utf-8"
            ) as file:
                file.seek(0)
                existing_words = file.read().splitlines()
                if word not in existing_words:
                    file.write(
                        word.replace(".", "").replace(",", "").replace(":", "") + "\n"
                    )
    if highlighted:
        os.makedirs(output_images_path, exist_ok=True)
        output_path = output_images_path + "/" + image_path.split("/")[-1]
        image.save(output_path)
        print(f"Annotated image saved to: {output_path}")
