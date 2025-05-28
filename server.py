from mcp.server.fastmcp import FastMCP
from app import searchRecipes

# Initialize MCP server
mcp = FastMCP("recipe-search-mcp")

@mcp.tool()
async def search_recipes(
    query: str,
    api_key: str,
    cuisine: str = None,
    diet: str = None,
    maxReadyTime: int = None,
    maxCalories: int = None,
    number: int = 10
) -> dict:
    """
    Search through thousands of recipes using advanced filtering and ranking.
    
    Args:
        query: The (natural language) recipe search query (required)
        api_key: Spoonacular API key (required)
        cuisine: The cuisine(s) of the recipes (optional, e.g., "italian", "mexican")
        diet: The diet(s) for which the recipes must be suitable (optional, e.g., "vegetarian", "vegan")
        maxReadyTime: Maximum time in minutes to prepare and cook (optional)
        maxCalories: Maximum calories per serving (optional)
        number: Number of expected results (1-100, default 10)
    
    Returns:
        dict: Recipe search results or error message
    """
    # Call the function from app.py with simplified parameters
    result = searchRecipes(
        query=query,
        cuisine=cuisine,
        diet=diet,
        maxReadyTime=maxReadyTime,
        maxCalories=maxCalories,
        number=number,
        api_key=api_key
    )
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")