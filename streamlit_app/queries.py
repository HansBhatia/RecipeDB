food_to_recipe_id = "SELECT recipeId FROM Ingredients WHERE foodId = (SELECT foodId FROM Food WHERE name = {})"
recipe_to_recipe_id = "SELECT * from Recipe WHERE name = {}"
recipe_from_id = "SELECT * from Recipe as r, {} as query WHERE r.recipeId = query.recipeId"
get_top_n_recipes = "SELECT * FROM Recipe as r, Rating as n WHERE r.recipeId = n.recipeId ORDER BY n.value DESC limit {}"
user_add_rating ="INSERT INTO Rating (userId, recipeId, value) VALUES ({}, {}, {}) ON DUPLICATE KEY UPDATE value = {};"
recipe_id_to_rating ="SELECT nr FROM NumRatings WHERE recipeId = {};"
#NumRatings