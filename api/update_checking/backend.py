from fastapi import FastAPI

app = FastAPI()

CURRENT_VERSION = "1.0.1"

@app.get("/version/")
def get_version():
    return {"version": CURRENT_VERSION}
