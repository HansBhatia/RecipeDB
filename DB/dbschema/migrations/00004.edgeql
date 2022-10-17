CREATE MIGRATION m142cz3tamzgdya3hwkknc4h3uhywwcqeiirxg6tuefzuuie3tiz2a
    ONTO m1b5izlxgeoxyzjcaumqsiworj7vbqz5ou5ttbtmiaixo66dmqkfbq
{
  ALTER TYPE default::DietaryRestrictions {
      CREATE PROPERTY type -> std::str;
  };
  CREATE TYPE default::FavoriteRecipes {
      CREATE MULTI LINK recipeid -> default::Recipe;
      CREATE REQUIRED SINGLE LINK userid -> default::User;
  };
  ALTER TYPE default::Ingredients {
      DROP PROPERTY recipeid;
  };
  ALTER TYPE default::Ingredients {
      CREATE MULTI LINK recipeid -> default::Recipe;
  };
  ALTER TYPE default::Ingredients {
      DROP PROPERTY calories_per_portion;
  };
  ALTER TYPE default::Ingredients {
      DROP PROPERTY price_per_portion;
  };
  ALTER TYPE default::Recipe {
      DROP LINK calories_per_portion;
  };
  ALTER TYPE default::Recipe {
      DROP LINK price_per_portion;
  };
  ALTER TYPE default::Recipe {
      DROP LINK recipeid;
  };
  ALTER TYPE default::Recipe {
      CREATE REQUIRED PROPERTY recipeid -> std::int16 {
          SET REQUIRED USING (1);
      };
  };
};
