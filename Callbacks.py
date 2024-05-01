import mysql.connector as connector
import pymongo
import bcrypt

bcrypt_secret = b's$cret12oaisjdpqhd-9jawpj-9qjd-19h2eh0q9jd-192jd-asjcpospchz0xinczmcpomas-djqw-9r-qhtsdnfajsf0ashgi0ewhc8ym8tcna90nchf90a'

salt = bcrypt.gensalt()


connection  = connector.connect(
    host="",
    user="",
    password="",
    database=""
)


sql_cursor = connection.cursor()


mongo = pymongo.MongoClient()



def SignIn(email,password):

    if not (email and password) :
        return {
            'status':-1,
            'error':'Invalid Data',
            'data':None
        }

    sql_cursor.execute(f"select * from users where email={email}")
    user = sql_cursor.fetchone()
    # user = sql_cursor.fetchone()

    # we check if the user actually exists(correct email)
    isCorrectLogin = bcrypt.checkpw(password, user['hashedPassword'])

    if(not isCorrectLogin) :
        return {
            'status':-2,
            'error':'Invalid Credentials',
            'data':None
        }




    return user



def CreateStudent(currentID,data):
    sql_cursor.execute(f"select * from users where id={currentID}")
    adminCandidate = sql_cursor.fetchone()
    if(adminCandidate['role']!= 'admin'):
        return {
            'status':-1,
            'error':'Not Authorized',
            'data':None
        }


    sql_cursor.execute(f'select * from users where email={data.email}')

    user = sql_cursor.fetchone()
    # we check if the user actually exists(correct email)
    if(user and user['hashedPassowrd']):
        return {
            'status':-2,
            'error':'User Already Exists',
            'data':user
        }

    # isCorrectLogin  = bcrypt.checkpw(data.password,user['hashedPassword'])
    sql_cursor.execute('insert into users values()')

    ret_data = sql_cursor.fetchone()


    return {
            'status':0,
            'error':'Created Successfully',
            'data':ret_data
        }





