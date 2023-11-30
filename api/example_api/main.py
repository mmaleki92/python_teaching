from typing import Union
from fastapi import FastAPI
import random

app = FastAPI()

'127.0.0.1:8000/product/dkp-12790241'
@app.get("/product/{p_id}")
def read_item(p_id: int, q: Union[str, None] = None):
    return {"item_id": random.randint(0, 100)}