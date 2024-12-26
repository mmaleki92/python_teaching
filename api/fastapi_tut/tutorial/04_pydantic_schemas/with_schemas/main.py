from fastapi import FastAPI, APIRouter, Query, HTTPException
from typing import Optional, List
from schemas import RecipeSearchResults, Recipe, RecipeCreate
from recipe_data import RECIPES

app = FastAPI(
    title="Recipe API",
    description="An API for searching, retrieving, and creating recipes.",
    version="1.0.0",
    openapi_url="/openapi.json",
)

# API router
api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET endpoint.
    Returns a welcome message.
    """
    return {"msg": "Hello, World!"}


@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(recipe_id: int) -> Recipe:
    """
    Fetch a single recipe by ID.
    """
    result = next((recipe for recipe in RECIPES if recipe["id"] == recipe_id), None)
    if not result:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return Recipe(**result)

@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    keyword: Optional[str] = Query(
        None,
        min_length=3,
        description="Keyword to search for in recipe labels.",
        examples={
            "chickenExample": {
                "summary": "A chicken search example",
                "value": "chicken",
            }
        },
    ),
    max_results: int = Query(
        10, ge=1, le=50, description="Maximum number of results to return."
    ),
) -> RecipeSearchResults:
    """
    Search for recipes based on label keyword.
    """
    if not keyword:
        return RecipeSearchResults(results=RECIPES[:max_results])

    filtered_recipes = [
        recipe for recipe in RECIPES if keyword.lower() in recipe["label"].lower()
    ]
    return RecipeSearchResults(results=filtered_recipes[:max_results])

@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(recipe_in: RecipeCreate) -> Recipe:
    """
    Create a new recipe (in-memory only).
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.dict())
    return recipe_entry

# Include the router
app.include_router(api_router)

if __name__ == "__main__":
    # Use uvicorn for debugging
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)
