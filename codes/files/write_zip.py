import zipfile

with zipfile.ZipFile("example.zip", "w") as archive:
    archive.write("example.txt")