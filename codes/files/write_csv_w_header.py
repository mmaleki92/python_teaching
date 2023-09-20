import csv

data = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
]

with open("example.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)