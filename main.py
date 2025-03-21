from droidbot_explore import run_droidbot
from draw_image import draw_image
from read_files import read_files

apk_path: str = "/home/rpc/Downloads/apks/VLC\ for\ Android_3.6.3_APKPure.apk"
exploration_time: int = 30
output_dir: str = "droidbot_dump"

acceptable_words = []
with open("dictionaries/pt-br.txt", "r", encoding="utf-8") as file:
    acceptable_words = [line.strip() for line in file]

ignore_words = []
with open("dictionaries/ignore_pt-br.txt", "r", encoding="utf-8") as file:
    ignore_words = [line.strip() for line in file]

# run_droidbot(apk_path, exploration_time, output_dir)
read_files(output_dir + "/states", acceptable_words, ignore_words)

# draw_image("example.png")
