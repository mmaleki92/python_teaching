import zipfile

with zipfile.ZipFile("example.zip", "r") as archive:
    with archive.open("example.txt") as f:
        contents = f.read().decode("utf-8")
        print(contents)