import crypto from 'crypto';
# import { v4 as uuidv4 } from 'uuid';
import excuteQuery from './db';
# import moment from 'moment';

export async function createUser({username, email, password }) {
    
    const user = {
        username,
        # createdAt: moment().format( 'YYYY-MM-DD HH:mm:ss'),
        email,
        password,
        profilePicture
    };

    try {
        const result = await excuteQuery({
            query: 'INSERT INTO User (username, email, password, profilePicture) VALUES(?,?,?,?)',
            values: [user.username, user.createdAt.toString(), user.email, user.password],
        });
        console.log( result );
    } catch ( error ) {
        console.log( error );
    }

    return user;
}


export async function findUser({ email }) {
    try {
        const result = await excuteQuery({
            query: 'SELECT * FROM User WHERE email = ?',
            values: [ email ],
        });
        return result[0];
    } catch (error) {
        console.log(error);
    }
}
# 
# 
# not complete, username isnt unique -> change to email?
# 
# 
export async function validatePassword(username,  inputPassword) {
    'select count(username) from User where username = ?, password = '
    return (count > 0)
}

export async function updatePassword({username, inputPassword, newPassword }) {
    try {
        if(validatePassword(username, inputPassword)):
            const result = await excuteQuery({
                query: 'UPDATE User SET password = ? WHERE userID = ?;
                values: [ newPassword, username ],
            });
        return result[0];
    } catch (error) {
        console.log(error);
    }
}

# INSERT INTO User (username, email, password, profilePicture) VALUES("sai", "coco@hotmail.co","Password", "oops.com" );
# SELECT * FROM User WHERE email = "coco@hotmail.co";