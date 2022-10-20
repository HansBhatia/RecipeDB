import db

def createUser(username, email, password, profilePicture):
    try:
        resp = db.query(f'INSERT INTO User (username, email, password, profilePicture) VALUES("{username}","{email}","{password}","{profilePicture}")', insert=True)
        return findUser(username)
    except Exception as e:
        print(e)
        return []


def findUser(username):
    try:
        resp = db.query(f"SELECT * FROM User WHERE username = '{username}'")[0] # since unique
        user = {
            'id': resp[0],
            'username': resp[1],
            'email': resp[2],
            'password': resp[3],
            'profilePicture': resp[4]
        }
        return user;
    except Exception as e:
        print(e)
        return []
    


def validatePassword(username, inputPassword):
    try:
        resp = db.query(f"SELECT COUNT(username) FROM User WHERE (username = '{username}' AND password = '{inputPassword}')")
    except Exception as e:
        print(e)
        return []
    return findUser(username)


def updatePassword(username, inputPassword, newPassword):
    try:
        if(validatePassword(username, inputPassword)):
            resp = db.query(f"UPDATE User SET password = '{newPassword}' WHERE username = '{username}'")
        return result[0]
    except Exception as e:
        print(e)
        return []