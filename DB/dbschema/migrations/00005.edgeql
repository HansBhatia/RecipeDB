CREATE MIGRATION m1zhcpklj55fufprisu6epotchfrawtehb55pwn5rtwatkipn5hprq
    ONTO m142cz3tamzgdya3hwkknc4h3uhywwcqeiirxg6tuefzuuie3tiz2a
{
  ALTER TYPE default::Recipe {
      CREATE PROPERTY calories -> std::int16;
      CREATE PROPERTY image -> std::str;
      CREATE PROPERTY prepSteps -> array<std::str>;
  };
};
