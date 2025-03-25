from droidbot_explore import run_droidbot
from draw_image import draw_image
from read_files import read_files
from remove_duplicates import remove_duplicates

apk_path: str = "/home/rpc/Downloads/apks/VLC\ for\ Android_3.6.3_APKPure.apk"
exploration_time: int = 30
output_directory: str = "output_images"

acceptable_words = []
with open("dictionaries/pt-br.txt", "r", encoding="utf-8") as file:
    acceptable_words = [line.strip() for line in file]

ignore_words = []
with open("dictionaries/ignore_pt-br.txt", "r", encoding="utf-8") as file:
    ignore_words = [line.strip() for line in file]

# run_droidbot(apk_path, exploration_time, "droidbot_dump")

# Example usage
image_directory = "/home/rpc/Desktop/l10n-auto/droidbot_dump/states"
remove_duplicates(image_directory)
read_files("droidbot_dump" + "/states", acceptable_words, ignore_words)

draw_image("example.png", output_directory, [])
