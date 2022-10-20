import json
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# lmao .env didn't work xd
mydb = mysql.connector.connect(
    host = os.getenv('DB_HOSTNAME'),
    user = os.getenv('DB_USER'),
    password =  os.getenv('DB_PASSWORD'),
    database =  os.getenv('DB_NAME')
)
mycursor = mydb.cursor(buffered = True)

def populateDBFromJSON(filename):
    data = {}
    with open(filename) as f:
        data = json.load(f)
    
    for _, recipes in data.items():
        for recipeName, recipeFields in recipes.items():
            # Adding new recipe
            sql = 'INSERT INTO Recipe (name, cuisine, calories, time, instructions, image) VALUES ("{}", "{}", "{}", {}, "{}", "{}");'.format(
                recipeName,
                recipeFields['cuisineType'],
                recipeFields['calories'],
                int(recipeFields['totalTime']),
                recipeFields['url'],
                recipeFields['image']
            )
            mycursor.execute(sql)

            sql = "SELECT recipeId FROM Recipe WHERE name = '{}';".format(
                recipeName
            )
            mycursor.execute(sql)
            recipeId = mycursor.fetchall()[0][0]

            # Adding food items and ingredients
            ingredients = recipeFields['ingredients']
            for ingredient in ingredients:
                sql = "INSERT IGNORE INTO Food (foodId, name) VALUES ('{}', '{}');".format(
                    ingredient["foodId"],
                    ingredient["food"]
                )
                mycursor.execute(sql)

                measure = ingredient["measure"]
                sql = "INSERT IGNORE INTO Ingredients (recipeId, foodId, measure, quantity) VALUES ({}, '{}', {}, {});".format(
                    recipeId,
                    ingredient["foodId"],
                    "null" if not measure or measure == "<unit>" else f"'{measure}'",
                    ingredient["quantity"]
                )
                mycursor.execute(sql)
            
            # Adding food restrictions
            for healthLabel in recipeFields['healthLabels']:
                sql = "INSERT INTO RecipeRestrictions (recipeId, restrictionId) VALUES ({}, (SELECT restrictionId FROM DietRestrictions WHERE name = '{}'));".format(
                    recipeId,
                    healthLabel
                )
                mycursor.execute(sql)
            mydb.commit()
    

if __name__ == '__main__':
    populateDBFromJSON('recipes.json')