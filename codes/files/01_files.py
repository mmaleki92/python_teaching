
# pip install pillow

# Read file
with open("input.txt", "r") as file:
    data = file.read()

# Write file
with open("output.txt", "w") as file:
    file.write("Data: " + data)


# Open file in read mode
with open("example.txt", "r") as file:
    # Read the entire contents of the file
    content = file.read()
    print(content)


# Open file in write mode
with open("output.txt", "w") as file:
    # Write content to the file
    file.write("This is some text that will be written to the file.")


# Open file in append mode
with open("output.txt", "a") as file:
    # Append content to the file
    file.write("\nThis line will be appended to the file.")
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import csv

data = [
    ['Name', 'Age', 'Country'],
    ['John', 25, 'USA'],
    ['Emily', 30, 'Canada'],
    ['James', 27, 'UK']
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)



import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
import json

data = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

with open("output.json", "w") as file:
    json.dump(data, file)


with open("image.jpg", "rb") as file:
    data = file.read()
    # Process binary data



from PIL import Image

# Open the image file
with Image.open("input.jpg") as image:
    # Display image properties
    print("Image format:", image.format)
    print("Image size:", image.size)
    print("Image mode:", image.mode)

    # Show the image
    image.show()


from PIL import Image
# Open the image file
with Image.open("input.jpg") as image:
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Save the grayscale image
    grayscale_image.save("output.jpg")

    # Show the grayscale image
    grayscale_image.show()
