import mysql.connector

def query():
    cnx = mysql.connector.connect(
        user='recipeApp',
        password='cS348!project',
        host='165.232.138.171',
        database='main'
    )
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM DietRestrictions')
    response = cursor.fetchall()
    cursor.close()
    cnx.close()
    return response