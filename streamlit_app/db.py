import mysql.connector

def query(q: str):
    cnx = mysql.connector.connect(
        user='recipeApp',
        password='cS348!project',
        host='165.232.138.171',
        database='main'
    )
    cursor = cnx.cursor()
    try:
        cursor.execute(q)
        #cursor.execute('SELECT * from DietRestrictions;')
    except:
        return []

    response = cursor.fetchall()
    print(response)
    cursor.close()
    cnx.close()
    return response