# RecipeDB
Milestone 2 Notes:
* Please change to use the stable_M2 branch for milestone 2. The main branch may have files not associated with M2.
* Our application can be found at: http://35.93.145.199:8501/.

## C1
### Steps to create and load sample database:
This database is hosted on a MySQL server. The database information in the `/data/scripts/connectDB.py` file (lines 8 - 13). If you want to create and load a copy of the sample database:
* Modify the database information in `/data/scripts/connectDB.py`.
* Run the queries in `/queries/initDB.sql`.
* Change directories to the `/data` directory.
* Run `python applyMigrations.py`, passing in any number of additional command line arguments corresponding to keywords that correspond to files in `/data/json`. For example, to populate the database with burger and pizza recipes, run `python applyMigrations.py burger pizza`.
### Steps to access and deploy the application:
From the repository directory run these commands on the terminal.   
`cd streamlit_app`
`pip install -r requirements.txt`

Once done simply run the command on the terminal.
`streamlit run main.py`

Access the url http://localhost:8501 or the url that was given after the streamlit run command. (The app is now deployed).
### Features currently supported:
All of the features described in the report are currently supported. That is, features R6 - R11 are all supported.

## C2
Relevant SQL files/scripts are as follows:
* `/queries/initDB.sql` contains all the queries for creating tables, indexes and views.
* `/queries/clearDB.sql` drops all of the tables and views.
* `/data/migrations/base/populateDietRestrictions.sql` populates the DietRestrictions table.
* `/data/migrations/recipe` contains all the relevant SQL statements for populating the database with the recipes.
* `/data/migrations/test/populateTestUsers.sql` populates the DB with test users.

## C3
The SQL statements listed in the report.pdf document can be found in `/queries/test-sample/test-sample.sql` and the output of these queries can be found in `/queries/test-sample/test-sample.out`.

Other queries that can be used to query the DB (outside of those presented in the report.pdf document) are in `/queries/recipeQueries.sql` and `/queries/userQueries.sql`.

## C4
The SQL statements listed in the report.pdf document can be found in `/queries/test-production/test-production.sql` and the output of these queries can be found in `/queries/test-production/test-production.out`.

## C5
All of the application code that implements the claimed feature for M1 are in `/streamlit_app`.

## Code for Downloading/Transforming Data
Scripts corresponding to the database migration pipeline, or R16: fancy feature 5 can be found in the `/data` folder. These scripts inlude scripts that query the API for recipes, transform the queried data into JSON files, and populate the database with the extracted recipe data. The description and usage notes for these files can also be found in the README in the same location.