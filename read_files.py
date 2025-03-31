import json
import os
from check_word import check_word
from draw_image import draw_image


def read_files(
    files_dir: str,
    acceptable_list: list,
    ignore_list: list,
    output_directory: str = "output_images",
) -> None:
    json_files = [f for f in os.listdir(files_dir) if f.endswith(".json")]
    for json_file in json_files:
        file_name = os.path.splitext(json_file)[0]
        not_acceptable_words = []
        print(f"Reading file: {file_name}")
        all_words_in_file = read_json_file(f"{files_dir}/{json_file}")
        for word in all_words_in_file:
            if not check_word(word, acceptable_list, ignore_list):
                # print(f"word: {word} is not acceptable")
                not_acceptable_words.append(word)
        image_name = file_name.replace("state", "screen")
        draw_image(
            f"{files_dir}/{image_name}.png", output_directory, not_acceptable_words
        )
        print("\n\n")


def read_json_file(file_path: str):
    all_words = []
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        views = data["views"]
        for view in views:
            text = view.get("text")
            if text is None:
                continue
            text = text.strip().replace("\n", " ")
            words = text.split(" ")
            all_words.extend(words)
    return all_words
