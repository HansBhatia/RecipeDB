-- R6
SELECT * FROM Recipe WHERE recipeId IN (SELECT recipeId FROM Ingredients WHERE foodId = (SELECT foodId FROM Food WHERE name = "Chicken"));

-- R7
SELECT * FROM Recipe WHERE name = 'Chicken Vesuvio';

-- R8
SELECT * FROM Recipe WHERE recipeId IN (SELECT recipeId FROM RecipeRestrictions WHERE restrictionId IN (SELECT restrictionId FROM DietRestrictions WHERE name = 'Peanut-Free'));

-- R9
SELECT * FROM Recipe AS r, NumRatings AS nr WHERE r.recipeId = nr.recipeId ORDER BY nr DESC LIMIT 3;

-- R10
INSERT INTO User (username, email, password, profilePicture) VALUES ('User6', 'user6@fakeemail.com', 'User6', 'pic');

-- R11
SELECT recipeId FROM FavoriteRecipes WHERE userid = 2;