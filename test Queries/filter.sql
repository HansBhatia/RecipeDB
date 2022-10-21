
Select *
FROM Recipe
where recipeId in (select recipeId
                    from RecipeRestrictions
                    where restrictionId iN (select restrictionId
                                            from DietRestrictions
                                            where name = "Peanut-Free"))


