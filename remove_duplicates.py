import os
import json
from typing import Tuple


def remove_duplicates(files_dir: str) -> Tuple[int, int]:
    removed = 0
    json_files = [f for f in os.listdir(files_dir) if f.endswith(".json")]
    total = len(json_files)
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
                removed += 1
                image_name = file_name.replace("state", "screen")
                if os.path.exists(f"{files_dir}/{image_name}.png"):
                    os.remove(f"{files_dir}/{image_name}.png")
    return (total, removed)
