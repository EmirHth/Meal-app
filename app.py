import requests

def searchRecipes(query=None, cuisine=None, diet=None, maxReadyTime=None, 
                 maxCalories=None, number=10, api_key=None):
    """
    Search through thousands of recipes using advanced filtering and ranking.
    
    Args:
        query (str): The (natural language) recipe search query
        cuisine (str): The cuisine(s) of the recipes (comma separated)
        diet (str): The diet(s) for which the recipes must be suitable
        maxReadyTime (int): Maximum time in minutes to prepare and cook
        maxCalories (int): Maximum calories per serving
        number (int): Number of expected results (1-100, default 10)
        api_key (str): Spoonacular API key
    
    Returns:
        dict: Recipe search results or error message
    """
    # Build the API URL with f-string formatting
    api_url = (
        f"https://api.spoonacular.com/recipes/complexSearch"
        f"?apiKey={api_key}&number={number}"
    )
    
    # Build additional parameters
    params = []
    
    if query:
        params.append(f"query={query}")
    if cuisine:
        params.append(f"cuisine={cuisine}")
    if diet:
        params.append(f"diet={diet}")
    if maxReadyTime:
        params.append(f"maxReadyTime={maxReadyTime}")
    if maxCalories:
        params.append(f"maxCalories={maxCalories}")
    
    # Add additional parameters to URL
    if params:
        api_url += "&" + "&".join(params)
    
    try:
        # Make the API request
        response = requests.get(api_url)
        
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
