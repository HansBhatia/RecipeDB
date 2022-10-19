-- Drop index queries (not needed if dropping tables)
ALTER TABLE Recipe DROP INDEX IDX_cuisine;
ALTER TABLE FavoriteRecipes DROP INDEX IDX_userId;
ALTER TABLE Rating DROP INDEX IDX_recipeId;
ALTER TABLE Ingredients DROP INDEX IDX_recipeId;
ALTER TABLE Ingredients DROP INDEX IDX_foodId;
ALTER TABLE RecipeRestrictions DROP INDEX IDX_recipeId;
ALTER TABLE RecipeRestrictions DROP INDEX IDX_restrictionId;

DROP TABLE Recipe;
DROP TABLE User;
DROP TABLE FavoriteRecipes;
DROP TABLE Rating;
DROP TABLE Food;
DROP TABLE Ingredients;
DROP TABLE DietRestrictions;
DROP TABLE RecipeRestrictions;
