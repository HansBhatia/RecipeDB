SELECT * 
FROM Recipe 
WHERE recipeId IN (
                    SELECT recipeId 
                    FROM Ingredients 
                    WHERE foodId = (SELECT foodId 
                                    FROM Food 
                                    WHERE name = {'chicken'}))
