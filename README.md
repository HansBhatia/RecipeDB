# RecipeDB
Milestone 1 Notes:
* Please change to use the M1 branch for milestone 1. The main branch may have files not associated with M1.
* In the report, we have indicated that we have results for the test-sample.out file stored in different .out locations. These have all been consolidated to the `/queries/test-sample.out` file.

## C1
### Steps to create and load sample database:
This database is hosted on a MySQL server. The database information in the `/data/populateDB.py` file (lines 9 - 12). If you want to create and load a copy of the sample database:
* Modify the database information in `/data/populateDB.py`.
* Run the queries in `/queries/initDB.sql` and `/queries/populate/populateDietRestrictions.sql`, in that order.
* Run `/data/populateDB.py`
* Run the queries in `/queries/populate/populateTestUsers.sql`.
### Steps to access and deploy the application:
From the repository directory run these commands on the terminal.   
`cd streamlit_app
 pip install -r requirements.txt`
  - once done simply run the command on the terminal.
`streamlit run main.py`
Access the url http://localhost:8501 or the url that was given after the streamlit run command. (The app is now deployed).
### Features currently supported:
From the features described in the report, the following are implemented:
* R6: Users are able to enter a list of ingredients and get a list of recipes that use those ingredients.
* R7: Users can enter a recipe name and get the details for the specific recipe they requested.
* R9: Users are able to view the most popular recipes.
* R10: Users can create a new account on the website and sign in.
* R11: Users, after signing in, can indicate which recipes are their favorites and view a list of them in a designated tab.

## C2
Relevant SQL files/scripts are as follows:
* `/queries/initDB.sql` contains all the queries for creating tables, indexes and views.
* `/queries/clearDB.sql` drops all of the tables and views.
* `/queries/populate/populateDietRestrictions.sql` populates the DietRestrictions table.
* `/data/populateDB.py` populates the DB with recipes.
* `/queries/populate/populateTestUsers.sql` populates the DB with test users.

## C3
The SQL statements listed in the report.pdf document can be found in `/queries/test-sample/test-sample.sql` and the output of these queries can be found in `/queries/test-sample/test-sample.out`.

Other queries that can be used to query the DB (outside of those presented in the report.pdf document) are in `/queries/recipeQueries.sql` and `/queries/userQueries.sql`.

## C4
N/A for M1.

## C5
All of the application code that implements the claimed feature for M1 are in `/streamlit_app`.
