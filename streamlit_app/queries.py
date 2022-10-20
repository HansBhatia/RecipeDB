food_to_recipe_id = "SELECT recipeId FROM Ingredients WHERE foodId = (SELECT foodId FROM Food WHERE name = {})"
recipe_to_recipe_id = "SELECT * from Recipe WHERE name = {}"
recipe_from_id = "SELECT * from Recipe, {} as query WHERE id = query.recipeId"