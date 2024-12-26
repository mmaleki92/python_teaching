import requests

# API endpoint
url = "http://0.0.0.0:8001/recipe/"

# Data for the new recipe
new_recipe = {
    "label": "Spaghetti Carbonara",
    "source": "Chef John",
    "url": "https://example.com/spaghetti-carbonara",
    "submitter_id": 1,
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
