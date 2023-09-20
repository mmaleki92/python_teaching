import json

with open("example.json", "r") as f:
    data = json.load(f)
    print(data)