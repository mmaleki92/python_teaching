import requests

# Define the base URL for the FastAPI application
base_url = "http://127.0.0.1:8000"

# Function to print the response content
def print_response(response):
    print("Status Code:", response.status_code)
    print("Response Content:", response.json())
    print("\n")

# GET: Read all items
response = requests.get(f"{base_url}/items")
print("GET /items:")
print_response(response)

# GET: Read a specific item by ID
item_id_to_read = 1
response = requests.get(f"{base_url}/items/{item_id_to_read}")
print(f"GET /items/{item_id_to_read}:")
print_response(response)

# POST: Create a new item
new_item = {"item_id": 4, "name": "Item 4"}
response = requests.post(f"{base_url}/items", json=new_item)
print("POST /items:")
print_response(response)

# PUT: Update an item by ID
item_id_to_update = 4
updated_item = {"item_id": item_id_to_update, "name": "Updated Item 4"}
response = requests.put(f"{base_url}/items/{item_id_to_update}", json=updated_item)
print(f"PUT /items/{item_id_to_update}:")
print_response(response)

# DELETE: Delete an item by ID
item_id_to_delete = 4
response = requests.delete(f"{base_url}/items/{item_id_to_delete}")
print(f"DELETE /items/{item_id_to_delete}:")
print_response(response)

# Additional Advanced Operations

# PATCH: Partial update of an item by ID
item_id_to_partial_update = 3
import requests

item_id = 3
updates = {"name": "Updated Item 3"}
url = f"http://127.0.0.1:8000/items/{item_id}"
response = requests.patch(url, json=updates)
print(response.json())
