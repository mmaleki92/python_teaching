import requests

# API endpoint
url = "http://0.0.0.0:8000/recipe/"

# Data for the new recipe (with invalid data)
new_recipe = {
    "label": "Spaghetti Carbonara",
    "source": "Chef John",
    "url": "not-a-valid-url",  # Invalid URL
    "submitter_id": "not-an-integer",  # Invalid data type
}

# Make the POST request
response = requests.post(url, json=new_recipe)

# Print the response
if response.status_code == 201:
    print("Recipe created successfully!")
    print(response.json())  # Print the newly created recipe
else:
    print(f"Failed to create recipe: {response.status_code}")
    print(response.json())  # Print error details
