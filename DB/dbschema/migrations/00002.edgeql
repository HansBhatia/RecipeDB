CREATE MIGRATION m1hlihirpwcla4ojp7ob7ap2xisys3ng5agsnbyygmqf7e2nzt7dpa
    ONTO m1kra5vg5qugvh2obnnomakw5aj7urhe2e2evzfsytn2ze2aphfe7a
{
  ALTER TYPE default::Cusine {
      DROP PROPERTY cusineid;
  };
  ALTER TYPE default::Cusine {
      DROP PROPERTY name;
  };
  DROP TYPE default::Cusine;
  CREATE TYPE default::DietaryRestrictions {
      CREATE PROPERTY name -> std::str;
      CREATE REQUIRED PROPERTY restrictionid -> std::int16;
  };
  CREATE TYPE default::FoodRestriction {
      CREATE MULTI LINK restrictionid -> default::DietaryRestrictions;
      CREATE SINGLE LINK food_name -> default::Food;
  };
  ALTER TYPE default::Food {
      CREATE PROPERTY calories_per_unit -> std::int16;
  };
  ALTER TYPE default::Food {
      DROP PROPERTY foodid;
  };
  ALTER TYPE default::Food {
      ALTER PROPERTY name {
          RENAME TO food_name;
      };
  };
  ALTER TYPE default::Food {
      CREATE PROPERTY price_per_unit -> std::float32;
      CREATE PROPERTY unit -> std::str;
  };
  ALTER TYPE default::Ingredients {
      CREATE SINGLE LINK food_name -> default::Food;
  };
  ALTER TYPE default::Ingredients {
      DROP LINK name;
  };
  ALTER TYPE default::Ingredients {
      DROP PROPERTY unit;
  };
  ALTER TYPE default::Ingredients {
      CREATE SINGLE LINK unit -> default::Food;
  };
  ALTER TYPE default::Ingredients {
      CREATE PROPERTY amount -> std::int16;
  };
  ALTER TYPE default::Ingredients {
      CREATE PROPERTY calories_per_portion -> std::int16;
  };
  ALTER TYPE default::Ingredients {
      DROP PROPERTY portion;
  };
  ALTER TYPE default::Ingredients {
      ALTER PROPERTY price {
          RENAME TO price_per_portion;
      };
  };
  ALTER TYPE default::Ingredients {
      ALTER PROPERTY price_per_portion {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::Ingredients {
      CREATE REQUIRED PROPERTY recipeid -> std::int16 {
          SET REQUIRED USING (1);
      };
  };
  CREATE TYPE default::Rating {
      CREATE SINGLE LINK recipeid -> default::Recipe;
      CREATE REQUIRED PROPERTY timestamp -> std::datetime;
      CREATE PROPERTY value -> std::int16;
  };
  ALTER TYPE default::Recipe {
      CREATE SINGLE LINK calories_per_portion -> default::Ingredients;
      CREATE SINGLE LINK price_per_portion -> default::Ingredients;
      CREATE SINGLE LINK recipeid -> default::Ingredients;
      CREATE PROPERTY cuisine -> std::str;
      CREATE PROPERTY prepTime -> std::duration;
  };
};
