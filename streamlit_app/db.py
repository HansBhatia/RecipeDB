import mysql.connector
import streamlit as st

# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection(): # start a websocket to the database server
   return mysql.connector.connect(user = "recipeApp", password = "cS348!project", host = "165.232.138.171", database = "main")
   #return mysql.connector.connect(**st.secrets["db_credentials"])
cnx = init_connection()

# @st.experimental_memo(ttl=600)
def query(q: str, insert: bool = False): # query the database server
    print(q)
    try:
        cursor = cnx.cursor()
    except:
        cnx = init_connection()
        cursor = cnx.cursor()

    try:
        cursor.execute(q)
    except Exception as e:
        print(e)
        return []
    
    if insert:
        try:
            cnx.commit()
            print('commited')
        except Exception as e:
            print(e)
            return []

    response = cursor.fetchall()
    cursor.close()
    return response
