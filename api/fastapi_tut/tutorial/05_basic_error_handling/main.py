from fastapi import FastAPI, APIRouter, Query, HTTPException
from typing import Optional, List

from schemas import RecipeSearchResults, Recipe, RecipeCreate
from recipe_data import RECIPES

# Initialize the FastAPI app
app = FastAPI(
    title="Recipe API",
    description="An API to manage and search for recipes.",
    openapi_url="/openapi.json",
)

# Initialize the API router
api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root endpoint returning a welcome message.
    """
    return {"msg": "Hello, World!"}


@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(recipe_id: int) -> Recipe:
    """
    Retrieve a single recipe by its ID.
    Raises 404 if the recipe is not found.
    """
    recipe = next((recipe for recipe in RECIPES if recipe["id"] == recipe_id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe with ID {recipe_id} not found")
    return Recipe(**recipe)


@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    keyword: Optional[str] = Query(
        None,
        min_length=3,
        description="Keyword to search in recipe labels.",
        examples={"example": {"summary": "Search for chicken recipes", "value": "chicken"}},
    ),
    max_results: int = Query(
        10,
        ge=1,
        le=50,
        description="Maximum number of results to return.",
    ),
) -> RecipeSearchResults:
    """
    Search for recipes by a keyword in their labels.
    If no keyword is provided, return the first `max_results` recipes.
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
    Create a new recipe in memory.
    Assigns a unique ID to the new recipe.
    """
    new_entry_id = len(RECIPES) + 1
    new_recipe = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(new_recipe.model_dump())
    return new_recipe


# Include the router in the app
app.include_router(api_router)

if __name__ == "__main__":
    # Run the application for debugging purposes
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
