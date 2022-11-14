# Data Folder

This folder contains all of the scripts that are used to extract data from the Edamam API, as well as the data itself. The purpose of each file is as follows:
* `extractAPI.py` provides functions to retrieve relevant recipe information from the Edamam API, given a list of search terms, in JSON format.
* `populateDB.py` provides functions to populate the database with the retrieved data from Edamam API, given a file path to a correctly formatted JSON file.