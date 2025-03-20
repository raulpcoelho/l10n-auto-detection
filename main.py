from droidbot_explore import run_droidbot, read_files
from draw_image import draw_image

apk_path: str = "/home/rpc/Downloads/apks/VLC\ for\ Android_3.6.3_APKPure.apk"
exploration_time: int = 30
output_dir: str = "droidbot_dump"

run_droidbot(apk_path, exploration_time, output_dir)
read_files(output_dir + "/states")

# draw_image("example.png")
