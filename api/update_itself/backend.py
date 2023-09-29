from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

LATEST_VERSION = "1.0.1"
FILE_PATH = "new_file/frontend_v1.0.1.py"

@app.get("/version/")
def get_version():
    return {"version": LATEST_VERSION}

@app.get("/download/")
def download_latest_version():
    return FileResponse(FILE_PATH, headers={"Content-Disposition": "attachment; filename=frontend.py"})
