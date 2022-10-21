# RecipeDB
Milestone 1 Notes:
* Please change to use the M1 branch for milestone 1. The main branch may have files not associated with M1.
* In the report, we have indicated that we have results for the test-sample.out file stored in different .out locations. These have all been consolidated to the `queries/test-sample.out` file.
## C1
### Steps to create and load sample database:
This database is hosted on a MySQL server. The database information in the `data/populateDB.py` file (lines 9 - 12). If you want to create and load a copy of the sample database:
* Modify the database information in `data/populateDB.py`.
* Run the queries in `queries/initDB.sql` and `queries/populate/populateDietRestrictions.sql`, in that order.
* Run `data/populateDB.py`
* Run the queries in `queries/populate/populateTestUsers.sql`.
### Steps to access and deploy the application:
From the repository directory run these commands on the terminal.   
`cd streamlit_app
 pip install -r requirements.txt`
  - once done simply run the command on the terminal.
`streamlit run main.py`
Access the url http://localhost:8501 or the url that was given after the streamlit run command. (The app is now deployed).
## C2
Relevant SQL files/scripts are as follows:
* `queries/initDB.sql` contains all the queries for creating tables, indexes and views.
* `queries/clearDB.sql` drops all of the tables and views.
* `queries/populate/populateDietRestrictions.sql` populates the DietRestrictions table.
* `data/populateDB.py` populates the DB with recipes.
* `queries/populate/populateTestUsers.sql` populates the DB with test users.
## C3
The SQL statements listed in the report.pdf document can be found in `queries/test-sample/test-sample.sql` and the output of these queries can be found in `queries/test-sample/test-sample.out`.

Other queries that can be used to query the DB (outside of those presented in the report.pdf document) are in `queries/recipeQueries.sql` and `queries/userQueries.sql`.

## C4
N/A for M1.

## C5
Recipe Database
   * Take input on whether to choose ingredient search or recipe search.

          * if we choose recipe search you can input a recipe name and get matching results,
          * else choosing ingredient search we can input ingrediant names separated with comma's to obtain results.
  * Takes Inputted leftover ingredients and Returns a list of Recipes available
  * Common recipe's searchable based on features.
  * Have features including "Preparation Time", "Rating", "Diet Preferance", "Cuisine", "Common meals", "Time of day" 
      readily available to filter on.
  * Recipe creation, updation and deletion on user
  * Personalised accounts with user login.

