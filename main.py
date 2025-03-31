import argparse
import os
from droidbot_explore import run_droidbot
from draw_image import draw_image
from read_files import read_files
from remove_duplicates import remove_duplicates

parser = argparse.ArgumentParser()
parser.add_argument(
    "--output-directory", "-o", help="Output images path", default="output_images"
)
parser.add_argument(
    "--exploration-time", "-e", help="Exploration time in seconds", default=30
)
parser.add_argument("--apk-path", "-a", help="APK file path", required=True)
parser.add_argument(
    "--skip-droidbot", "-s", action="store_true", help="Skip droidbot exploration"
)
args = parser.parse_args()


acceptable_words = []
with open("dictionaries/pt-br.txt", "r", encoding="utf-8") as file:
    acceptable_words = [line.strip() for line in file]

ignore_words = []
with open("dictionaries/ignore_pt-br.txt", "r", encoding="utf-8") as file:
    ignore_words = [line.strip() for line in file]

if not args.skip_droidbot:
    run_droidbot(args.apk_path, args.exploration_time, "droidbot_dump")

image_directory = "droidbot_dump/states"
total, removed = remove_duplicates(image_directory)
os.makedirs(args.output_directory, exist_ok=True)
with open(f"{args.output_directory}/removed.txt", "a+", encoding="utf-8") as file:
    file.write(f"Removed {removed} images from {total}\n")
read_files(
    "droidbot_dump" + "/states", acceptable_words, ignore_words, args.output_directory
)
