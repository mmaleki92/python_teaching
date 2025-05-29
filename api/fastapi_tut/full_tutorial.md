# FastAPI Tutorial: Building Modern APIs with Asynchronous Python

## Table of Contents
- [Introduction to FastAPI](#introduction-to-fastapi)
- [Getting Started](#getting-started)
- [Basic Endpoints](#basic-endpoints)
- [Path Parameters](#path-parameters)
- [Query Parameters](#query-parameters)
- [Request Body](#request-body)
- [Understanding Asynchronous Programming](#understanding-asynchronous-programming)
- [Implementing Async in FastAPI](#implementing-async-in-fastapi)
- [Dependency Injection](#dependency-injection)
- [Database Operations with Async](#database-operations-with-async)
- [Background Tasks](#background-tasks)
- [Testing FastAPI Applications](#testing-fastapi-applications)
- [Deployment Best Practices](#deployment-best-practices)

## Introduction to FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It was created by Sebastián Ramírez and first released in 2018.

### Key Features:
- **Fast**: Very high performance, on par with NodeJS and Go
- **Easy to Learn**: Intuitive design, minimizing code duplication
- **Fast to Code**: Increase the speed to develop features by 200-300%
- **Robust**: Get production-ready code with automatic interactive documentation
- **Standards-based**: Based on OpenAPI and JSON Schema
- **Built-in Async Support**: Native support for asynchronous operations

## Getting Started

### Installation

```bash
pip install fastapi uvicorn
```

FastAPI requires an ASGI server like Uvicorn to run:

```bash
pip install "uvicorn[standard]"
```

### Your First FastAPI Application

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Run the server:

```bash
uvicorn main:app --reload
```

Now visit http://127.0.0.1:8000/ in your browser and you'll see `{"Hello":"World"}`.

Visit http://127.0.0.1:8000/docs for automatic interactive API documentation.

## Basic Endpoints

### HTTP Methods

FastAPI provides decorators for all standard HTTP methods:

```python
@app.get("/")
def read_root():
    return {"message": "This is a GET request"}

@app.post("/")
def create_item():
    return {"message": "This is a POST request"}

@app.put("/")
def update_item():
    return {"message": "This is a PUT request"}

@app.delete("/")
def delete_item():
    return {"message": "This is a DELETE request"}

@app.patch("/")
def partial_update_item():
    return {"message": "This is a PATCH request"}
```

## Path Parameters

Path parameters are variable parts of a URL path:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

FastAPI performs data validation and conversion based on the type annotations.

## Query Parameters

Query parameters are key-value pairs after the `?` in a URL:

```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Access this with: `/items/?skip=20&limit=30`

## Request Body

Use Pydantic models to declare request body requirements:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict["price_with_tax"] = price_with_tax
    return item_dict
```

## Understanding Asynchronous Programming

### Synchronous vs Asynchronous

In synchronous programming, operations block execution until they complete. In asynchronous programming, operations can run independently of the main program flow.

### Why Async?

- **Performance**: Handle thousands of concurrent connections
- **Scalability**: Better resource utilization
- **Responsiveness**: Keep your application responsive even during I/O operations

### Python's Async Framework

Python implements asynchronous programming through:
- `async` and `await` keywords
- `asyncio` library
- Event loops

## Implementing Async in FastAPI

FastAPI has native support for asynchronous programming:

```python
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

### When to Use Async

Use `async def` when your endpoint:
- Makes network calls
- Performs database operations
- Makes file system operations
- Calls other services that might take time

### Simple Async Example

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/delay/{seconds}")
async def delay(seconds: int):
    await asyncio.sleep(seconds)
    return {"message": f"Waited for {seconds} seconds"}
```

## Dependency Injection

FastAPI's dependency injection system is fully compatible with async:

```python
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

## Database Operations with Async

### Using Databases with Async

```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import databases

# Database URL
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/db"

# Database instance
database = databases.Database(DATABASE_URL)

app = FastAPI()

# Events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Example endpoint
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    query = "SELECT id, name, email FROM users WHERE id = :user_id"
    user = await database.fetch_one(query=query, values={"user_id": user_id})
    if user:
        return user
    return {"message": "User not found"}
```

## Background Tasks

FastAPI allows you to execute operations in the background:

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks
):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent in the background"}
```

## Testing FastAPI Applications

FastAPI provides a TestClient based on `pytest`:

```python
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

For testing async functions:

```python
import pytest
import asyncio
from httpx import AsyncClient
from .main import app

@pytest.mark.asyncio
async def test_read_main_async():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

## Deployment Best Practices

### Running in Production

In production, you should use multiple worker processes:

```bash
uvicorn main:app --workers 4
```

### Using Gunicorn

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Docker Deployment

Example Dockerfile:

```dockerfile
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

## Advanced Async Concepts

### Concurrent Tasks

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

async def fetch_data(id: int):
    await asyncio.sleep(1)  # Simulating an API call
    return {"id": id, "data": f"Item {id} data"}

@app.get("/concurrent")
async def get_concurrent_data():
    # Run three tasks concurrently
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    return results
```

### Streaming Responses

```python
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def generate_numbers(limit: int):
    for i in range(limit):
        yield f"Number: {i}\n"
        await asyncio.sleep(0.1)

@app.get("/stream")
async def stream_numbers():
    return StreamingResponse(generate_numbers(20))
```

## Conclusion

FastAPI provides a modern, efficient way to build APIs with Python, fully leveraging the power of async programming. By combining type annotations with async capabilities, it offers both developer productivity and high performance.

Remember that not all code needs to be async. Use it where it matters most - for I/O bound operations like database queries, HTTP requests, and file operations.

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Async/Await in Python](https://docs.python.org/3/library/asyncio-task.html)
- [Starlette Documentation](https://www.starlette.io/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)