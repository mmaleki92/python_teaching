from fastapi import FastAPI, APIRouter

# Create the FastAPI application
app = FastAPI(
    title="Recipe API",
    description="An API for managing recipes.",
    version="1.0.0",
    openapi_url="/openapi.json"
)

# Create an API router
api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET endpoint.
    Returns a welcome message.
    """
    return {"msg": "Hello, World!"}

# Include the router in the application
app.include_router(api_router)

if __name__ == "__main__":
    # Use uvicorn to serve the app for debugging purposes
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)
