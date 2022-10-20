import requests
import pandas as pd
# import csv

def recipe_search(ingredient):
    app_id = '73cf0996'
    app_key = '4b789708cddb597453e31879162878ae'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

# Fields required from the Request Response Body:
# image url (probably the LARGE one)// image
# label// label
# calories // calories
# Ingredient lines // ingredientLines
#   quantity // ingredients.quantity
#   measure // ingredients.measure
#   food // ingredients.food
#   foodId // infgredients.foodID
#total time
# cuisineType // cuisineType
# instructions //instructions
# healthLabels // healthLabels
def mklist(n):
    for _ in range(n):
        yield []
def run():
    
    ingredient = input('Enter an ingredient: ')
    # max_no_of_calories = float(input('Enter the max amount of calories desired in recipe: '))
    
    # Creating empty lists
    image, label, cuisineType, calories, ingredientLines, instructions, healthLabels, url, totalTime= mklist(9)
    # ingrQuantity, ingrMeasure, ingrFood, ingrFood = mklist(4) 
    ingredients = [[]] # added extra for sanity

    # Servings //  yield add later
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        # result['calories'] < max_no_of_calories
        
        image.append(recipe['image'])
        label.append(recipe['label'])
        cuisineType.append(recipe['cuisineType'])
        calories.append(round(recipe['calories']))
        ingredientLines.append(recipe['ingredientLines'])
        url.append(recipe['uri'])
        totalTime.append(recipe['totalTime'])
        # ingrQuantity.append(recipe['ingredients[quantity]'])
        # ingrMeasure.append(recipe['ingredients[measure]'])
        # ingrFood.append(recipe['ingredients[food]'])
        # ingrFoodId.append(recipe['ingredients[foodId]'])

        ingredients.append(recipe['ingredients'])
        instructions.append(recipe['dishType'])
        healthLabels.append(recipe['healthLabels'])

        data = {
            'Label': label,
            'Image URL': image,
            'Cuisine': cuisineType,
            'NumCalories': calories,
            'ingredient Lines': ingredientLines,
            'Recipe URL': url,
            'Preparation Time': totalTime
            # 'Ingr Quantity': ingrQuantity
            # 'Ingr Measure': ingrMeasure
            # 'Ingr Name': ingrFood
            # 'Ingr Id': ingrFoodId

            # 'Ingredients' : ingredients,
            'Preparation instructions': instructions,
            'health Labels': healthLabels
            }
        df = pd.DataFrame(data, columns=['Label', 'Image URL', 'Cuisine', 'NumCalories', 'Preparation Time', 'ingredient Lines',  'Recipe URL', 'Preparation instructions', 'health Labels'])
        df.to_csv('recipeSet.csv')


run()
