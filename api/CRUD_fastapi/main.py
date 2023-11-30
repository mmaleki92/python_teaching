from fastapi import FastAPI
import random

app = FastAPI()

db = {"a": "d",
      "n": "s"}

# GET: Read all items
@app.get("/items/{item_id}", response_model=dict)
def read_items(item_id:int):
    return {"a": random.randint(0, 100)}
