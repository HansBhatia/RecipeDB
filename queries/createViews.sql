CREATE VIEW AvgRating AS
    SELECT recipeId, AVG(rating) AS ar
    FROM Rating
    GROUP BY recipeId;

CREATE VIEW NumRatings AS
    SELECT recipeId, COUNT(*) AS nr
    FROM Rating
    GROUP BY recipeId;