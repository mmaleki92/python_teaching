import requests

BASE_URL = "http://127.0.0.1:8001"

# Test the root endpoint
def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("Root endpoint:", response.status_code, response.json())


# Test fetching a specific recipe by ID
def test_fetch_recipe(recipe_id):
    response = requests.get(f"{BASE_URL}/recipe/{recipe_id}")
    print(f"Fetch Recipe ID {recipe_id}:", response.status_code, response.json())


# Test searching for recipes
def test_search_recipes(keyword=None, max_results=10):
    params = {"keyword": keyword, "max_results": max_results}
    response = requests.get(f"{BASE_URL}/search/", params=params)
    print(f"Search Recipes (keyword='{keyword}', max_results={max_results}):", response.status_code, response.json())


# Test creating a new recipe
def test_create_recipe(label, source, url):
    payload = {
        "label": label,
        "source": source,
        "url": url,
        "submitter_id": 1  # Assuming this is required
    }
    response = requests.post(f"{BASE_URL}/recipe/", json=payload)
    print("Create Recipe:", response.status_code, response.json())


# Run all tests
if __name__ == "__main__":
    # Test root endpoint
    test_root()

    # Test fetching existing and non-existing recipes
    test_fetch_recipe(1)  # Assuming recipe with ID 1 exists
    test_fetch_recipe(999)  # Non-existing recipe ID

    # Test searching for recipes
    test_search_recipes(keyword="chicken", max_results=5)  # Valid keyword
    test_search_recipes(keyword="xyz", max_results=5)  # Keyword with no results
    test_search_recipes()  # No keyword, default behavior

    # Test creating a new recipe
    test_create_recipe(
        label="Spaghetti Bolognese",
        source="Grandma's Cookbook",
        url="http://example.com/spaghetti-bolognese"
    )
