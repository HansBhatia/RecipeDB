import requests
import json

def getAPIrecipes(keyword, count):
    app_id = '73cf0996'
    app_key = '4b789708cddb597453e31879162878ae'
    result = requests.get(f'https://api.edamam.com/search?q={keyword}&to={count}&app_id={app_id}&app_key={app_key}')
    data = result.json()
    return data['hits']

recipeNameField = "label"

# All fields we want except for ingredients
requiredFields = [
    "image",
    "url",
    "healthLabels",
    "calories",
    "totalTime",
    "cuisineType"
]

ingredientsFieldName = "ingredients"

ingredientsRequiredFields = [
    "quantity",
    "measure",
    "food",
    "foodId"
]

# Returns dictionary in JSON format containing recipes corresponding to each
# keyword
def searchRecipes(keyword, count):
    retVal = {}
    results = getAPIrecipes(keyword, count)
    keywordRecipes = {}
    for recipe in results:
        recipe = recipe['recipe']

        curRecipe = {}
        recipeName = recipe[recipeNameField]

        # API can return same recipes with different capitalization, so this
        # filters those out.
        if recipeName.lower() in [k.lower() for k in keywordRecipes.keys()]:
            continue

        for field in requiredFields:
            rawValue = recipe[field]
            if field == "calories":
                rawValue = int(rawValue)
            elif field == "cuisineType":
                rawValue = rawValue[0]
            curRecipe[field] = rawValue
        
        ingredients = []
        alreadyAddedIngredientNames = []
        # This is assuming the ingredients for each recipe are returned as
        # an array
        for ingredient in recipe[ingredientsFieldName]:
            # API can return same ingredient multiple times, so this filters
            # duplicate ingredients out. This doesn't catch all duplicate
            # ingredients as the same ingredient can be named differently
            # (e.g. 'cooking oil' and 'oil').
            ingredientName = ingredient["food"].lower()
            if ingredientName in alreadyAddedIngredientNames:
                continue
            else:
                alreadyAddedIngredientNames.append(ingredientName)
            
            curIngredient = {}
            for field in ingredientsRequiredFields:
                curIngredient[field] = ingredient[field]
            ingredients.append(curIngredient)
        curRecipe[ingredientsFieldName] = ingredients
        keywordRecipes[recipeName] = curRecipe
    retVal[keyword] = keywordRecipes
    return retVal
