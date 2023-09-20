from pathlib import Path

file_path = Path("example.txt")
contents = file_path.read_text()
print(contents)