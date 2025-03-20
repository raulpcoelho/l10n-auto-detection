import json

with open("state_2025-03-19_204248.json", "r") as f:
    dados = json.load(f)
    views = dados["views"]
    for view in views:
        text = view.get("text")
        if text is not None:
            print(text)
