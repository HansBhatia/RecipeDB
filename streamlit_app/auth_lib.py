import db

def createUser(username, email, password, profilePicture):
    user = {
        'username': username,
        'email': email,
        'password': password,
        'profilePicture': profilePicture
    }
    try:
        resp = db.query(f'INSERT INTO User (`username`, `email`, `password`, `profilePicture`) VALUES("{username}","{email}","{password}","{profilePicture}")')
        print(resp)
        return user
    except:
        return []


def findUser(email):
    try:
        resp = db.query(f"SELECT * FROM User WHERE email = '{email}'")[0] # since unique
        user = {
            'username': resp[1],
            'email': resp[2],
            'password': resp[3],
            'profilePicture': resp[4]
        }
        return user;
    except:
        return []
    


def validatePassword(username, inputPassword):
    try:
        resp = db.query(f"SELECT COUNT(username) FROM User WHERE (username = '{username}' AND password = '{inputPassword}')")
    except:
        return False
    return (resp[0][0] > 0)


def updatePassword(username, inputPassword, newPassword):
    try:
        if(validatePassword(username, inputPassword)):
            resp = db.query(f"UPDATE User SET password = '{newPassword}' WHERE username = '{username}'")
        return result[0]
    except:
        return []