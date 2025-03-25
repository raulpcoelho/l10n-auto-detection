import os
import json


def remove_duplicates(files_dir: str) -> None:
    json_files = [f for f in os.listdir(files_dir) if f.endswith(".json")]
    for json_file in json_files:
        file_name = os.path.splitext(json_file)[0]
        with open(f"{files_dir}/{json_file}", "r", encoding="utf-8") as f:
            data = json.load(f)
            if (
                data["foreground_activity"].find("launcher") != -1
                or len(data["views"]) == 0
            ):
                print(f"Removing file: {json_file}")
                os.remove(f"{files_dir}/{json_file}")
                image_name = file_name.replace("state", "screen")
                if os.path.exists(f"{files_dir}/{image_name}.png"):
                    os.remove(f"{files_dir}/{image_name}.png")
