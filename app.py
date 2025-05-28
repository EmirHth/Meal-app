import requests

def searchRecipes(query=None, cuisine=None, diet=None, intolerances=None, 
                 includeIngredients=None, excludeIngredients=None, type=None,
                 maxReadyTime=None, minServings=None, maxServings=None,
                 maxCalories=None, minProtein=None, maxFat=None,
                 number=10, offset=0, api_key=None):
    """
    Search through thousands of recipes using advanced filtering and ranking.
    
    Args:
        query (str): The (natural language) recipe search query
        cuisine (str): The cuisine(s) of the recipes (comma separated)
        diet (str): The diet(s) for which the recipes must be suitable
        intolerances (str): A comma-separated list of intolerances
        includeIngredients (str): Comma-separated list of ingredients that should be used
        excludeIngredients (str): Comma-separated list of ingredients to exclude
        type (str): The type of recipe (e.g., main course, dessert)
        maxReadyTime (int): Maximum time in minutes to prepare and cook
        minServings (int): Minimum amount of servings
        maxServings (int): Maximum amount of servings
        maxCalories (int): Maximum calories per serving
        minProtein (int): Minimum protein in grams per serving
        maxFat (int): Maximum fat in grams per serving
        number (int): Number of expected results (1-100, default 10)
        offset (int): Number of results to skip (0-900, default 0)
        api_key (str): Spoonacular API key
    
    Returns:
        dict: Recipe search results or error message
    """
    # Define the API endpoint
    api_url = "https://api.spoonacular.com/recipes/complexSearch"
    
    # Build parameters dictionary
    params = {
        "number": number,
        "offset": offset
    }
    
    # Add optional parameters if provided
    if query:
        params["query"] = query
    if cuisine:
        params["cuisine"] = cuisine
    if diet:
        params["diet"] = diet
    if intolerances:
        params["intolerances"] = intolerances
    if includeIngredients:
        params["includeIngredients"] = includeIngredients
    if excludeIngredients:
        params["excludeIngredients"] = excludeIngredients
    if type:
        params["type"] = type
    if maxReadyTime:
        params["maxReadyTime"] = maxReadyTime
    if minServings:
        params["minServings"] = minServings
    if maxServings:
        params["maxServings"] = maxServings
    if maxCalories:
        params["maxCalories"] = maxCalories
    if minProtein:
        params["minProtein"] = minProtein
    if maxFat:
        params["maxFat"] = maxFat
    if api_key:
        params["apiKey"] = api_key
    
    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return {
                "success": True,
                "offset": data.get("offset", 0),
                "number": data.get("number", 0),
                "totalResults": data.get("totalResults", 0),
                "results": data.get("results", [])
            }
        else:
            # Handle HTTP errors
            return {
                "success": False,
                "error": f"API request failed with status code {response.status_code}",
                "message": response.text
            }
    except Exception as e:
        # Handle other errors
        return {
            "success": False,
            "error": "Failed to retrieve data from API",
            "message": str(e)
        }
