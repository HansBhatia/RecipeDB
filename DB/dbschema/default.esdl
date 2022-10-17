module default {
    
  type Food {
    required property food_name -> str;
    property unit -> str;
    property calories_per_unit -> int16;
    property price_per_unit -> float32;
  }

  type User {
    required property email -> str;
    required property userid -> int16;
    property username -> str;
  }

  type FavoriteRecipes {
    required single link userid -> User;
    multi link recipeid -> Recipe;
  }

  type Ingredients {
    multi link recipeid -> Recipe;
    single link food_name -> Food;
    single link unit -> Food;
    property amount -> int16;
  }

  type Recipe {
    required property recipeid -> int16;
    required property name -> str;
    property prepTime -> duration;
    property cuisine -> str;
  }

  type Rating {
    single link recipeid -> Recipe;
    required property timestamp -> datetime;
    property value -> int16;
  }


  type FoodRestriction {
    single link food_name -> Food;
    multi link restrictionid -> DietaryRestrictions;
  }

  type DietaryRestrictions {
    required property restrictionid -> int16;
    property name -> str;
    property type -> str;
  }
};