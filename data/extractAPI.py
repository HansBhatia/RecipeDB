import requests
import json

def getAPIrecipes(keyword):
    app_id = '73cf0996'
    app_key = '4b789708cddb597453e31879162878ae'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(keyword, app_id, app_key))
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
def searchRecipes(keywords):
    retVal = {}
    for keyword in keywords:
        results = getAPIrecipes(keyword)
        keywordRecipes = {}
        for recipe in results:
            recipe = recipe['recipe']

            curRecipe = {}
            recipeName = recipe[recipeNameField]
            for field in requiredFields:
                rawValue = recipe[field]
                if field == "calories":
                    rawValue = int(rawValue)
                elif field == "cuisineType":
                    rawValue = rawValue[0]
                curRecipe[field] = rawValue
            
            ingredients = []
            # This is assuming the ingredients for each recipe are returned as
            # an array
            for ingredient in recipe[ingredientsFieldName]:
                curIngredient = {}
                for field in ingredientsRequiredFields:
                    curIngredient[field] = ingredient[field]
                ingredients.append(curIngredient)
            curRecipe[ingredientsFieldName] = ingredients
            keywordRecipes[recipeName] = curRecipe
        retVal[keyword] = keywordRecipes
    return retVal


if __name__ == '__main__':
    keywords = ["chicken"]
    with open("recipes.json", "w") as f:
        json.dump(searchRecipes(keywords), f)
