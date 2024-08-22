from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
import random

app = FastAPI()

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/data", response_model=List[float])
async def get_data():
    # Generate random data for plotting
    data = [random.uniform(0, 100) for _ in range(10)]
    return data

@app.get("/", response_class=HTMLResponse)
async def get_html(request: Request):
    # Render the plot.html template
    return templates.TemplateResponse("plot.html", {"request": request})
