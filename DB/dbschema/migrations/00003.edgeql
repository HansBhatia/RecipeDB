CREATE MIGRATION m1b5izlxgeoxyzjcaumqsiworj7vbqz5ou5ttbtmiaixo66dmqkfbq
    ONTO m1hlihirpwcla4ojp7ob7ap2xisys3ng5agsnbyygmqf7e2nzt7dpa
{
  CREATE TYPE default::User {
      CREATE REQUIRED PROPERTY email -> std::str;
      CREATE REQUIRED PROPERTY userid -> std::int16;
      CREATE PROPERTY username -> std::str;
  };
};
