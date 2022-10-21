import mysql.connector
import streamlit as st

# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["db_credentials"])
cnx = init_connection()

@st.experimental_memo(ttl=600)
def query(q: str, insert: bool = False):
    cursor = cnx.cursor()
    try:
        cursor.execute(q)
        #cursor.execute('SELECT * from DietRestrictions;')
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