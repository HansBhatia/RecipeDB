CREATE MIGRATION m1kra5vg5qugvh2obnnomakw5aj7urhe2e2evzfsytn2ze2aphfe7a
    ONTO initial
{
  CREATE TYPE default::Cusine {
      CREATE REQUIRED PROPERTY cusineid -> std::int16;
      CREATE REQUIRED PROPERTY name -> std::str;
  };
  CREATE TYPE default::Food {
      CREATE REQUIRED PROPERTY foodid -> std::int16;
      CREATE REQUIRED PROPERTY name -> std::str;
  };
  CREATE TYPE default::Ingredients {
      CREATE MULTI LINK name -> default::Food;
      CREATE REQUIRED PROPERTY portion -> std::int16;
      CREATE REQUIRED PROPERTY price -> std::float32;
      CREATE REQUIRED PROPERTY unit -> std::str;
  };
  CREATE TYPE default::Recipe {
      CREATE REQUIRED PROPERTY name -> std::str;
  };
};
