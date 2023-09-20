import csv

data = [
    ["John", "Smith", "25"],
    ["Jane", "Doe", "30"],
]

with open("example.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)