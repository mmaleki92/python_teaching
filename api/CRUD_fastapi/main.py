from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data
db = {
    "items": [
        {"item_id": 1, "name": "Item 1"},
        {"item_id": 2, "name": "Item 2"},
        {"item_id": 3, "name": "Item 3"},
    ]
}

# GET: Read all items
@app.get("/items", response_model=list)
def read_items():
    return db["items"]

# GET: Read a specific item by ID
@app.get("/items/{item_id}", response_model=dict)
def read_item(item_id: int):
    item = next((item for item in db["items"] if item["item_id"] == item_id), None)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# POST: Create a new item
@app.post("/items", response_model=dict)
def create_item(item: dict):
    new_item_id = max(item["item_id"] for item in db["items"]) + 1
    item["item_id"] = new_item_id
    db["items"].append(item)
    return item

# PUT: Update an item by ID
@app.put("/items/{item_id}", response_model=dict)
def update_item(item_id: int, updated_item: dict):
    index = next((i for i, item in enumerate(db["items"]) if item["item_id"] == item_id), None)
    if index is not None:
        db["items"][index] = updated_item
        return updated_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# DELETE: Delete an item by ID
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    index = next((i for i, item in enumerate(db["items"]) if item["item_id"] == item_id), None)
    if index is not None:
        deleted_item = db["items"].pop(index)
        return deleted_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Additional Advanced Operations

# PATCH: Partial update of an item by ID
@app.patch("/items/{item_id}", response_model=dict)
def partial_update_item(item_id: int, updates: dict):
    index = next((i for i, item in enumerate(db["items"]) if item["item_id"] == item_id), None)
    if index is not None:
        db["items"][index].update(updates)
        return db["items"][index]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# HEAD: Check if an item exists by ID
@app.head("/items/{item_id}")
def check_item_exists(item_id: int):
    if any(item["item_id"] == item_id for item in db["items"]):
        return
    else:
        raise HTTPException(status_code=404, detail="Item not found")
