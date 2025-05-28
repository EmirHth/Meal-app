from mcp.server.fastmcp import FastMCP
from app import searchRecipes

# Initialize MCP server
mcp = FastMCP("recipe-search-mcp")

@mcp.tool()
async def search_recipes(
    query: str = None,
    cuisine: str = None,
    diet: str = None,
    intolerances: str = None,
    includeIngredients: str = None,
    excludeIngredients: str = None,
    type: str = None,
    maxReadyTime: int = None,
    minServings: int = None,
    maxServings: int = None,
    maxCalories: int = None,
    minProtein: int = None,
    maxFat: int = None,
    number: int = 10,
    offset: int = 0,
    api_key: str = None
) -> dict:
    """
    Search through thousands of recipes using advanced filtering and ranking.
    
    Args:
        query: The (natural language) recipe search query
        cuisine: The cuisine(s) of the recipes (comma separated)
        diet: The diet(s) for which the recipes must be suitable
        intolerances: A comma-separated list of intolerances
        includeIngredients: Comma-separated list of ingredients that should be used
        excludeIngredients: Comma-separated list of ingredients to exclude
        type: The type of recipe (e.g., main course, dessert)
        maxReadyTime: Maximum time in minutes to prepare and cook
        minServings: Minimum amount of servings
        maxServings: Maximum amount of servings
        maxCalories: Maximum calories per serving
        minProtein: Minimum protein in grams per serving
        maxFat: Maximum fat in grams per serving
        number: Number of expected results (1-100, default 10)
        offset: Number of results to skip (0-900, default 0)
        api_key: Spoonacular API key
    
    Returns:
        dict: Recipe search results or error message
    """
    # Call the function from app.py (remove await, since searchRecipes is sync)
    result = searchRecipes(
        query=query,
        cuisine=cuisine,
        diet=diet,
        intolerances=intolerances,
        includeIngredients=includeIngredients,
        excludeIngredients=excludeIngredients,
        type=type,
        maxReadyTime=maxReadyTime,
        minServings=minServings,
        maxServings=maxServings,
        maxCalories=maxCalories,
        minProtein=minProtein,
        maxFat=maxFat,
        number=number,
        offset=offset,
        api_key=api_key
    )
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")