import mysql.connector as connector
import pymongo
import bcrypt
from pymongo.server_api import ServerApi

bcrypt_secret = b's$cret12oaisjdpqhd-9jawpj-9qjd-19h2eh0q9jd-192jd-asjcpospchz0xinczmcpomas-djqw-9r-qhtsdnfajsf0ashgi0ewhc8ym8tcna90nchf90a'

salt = bcrypt.gensalt()


connection  = connector.connect(
    host="monorail.proxy.rlwy.net",
    user="root",
    password="EfSYqdABwcnRZMlenSDeXHQHgkjGYofR",
    port="52256",
    database="railway"
)



sql_cursor = connection.cursor()


mongo = pymongo.mongo_client.MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))


def getDb():
    return mongo['bddd']

def execute_query(collection,query):
    result = collection.find(query)
    return result



def validCurrentId(currentID):
    return not (currentID==None or currentID=='')


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
    if(not validCurrentId(currentID)):
        return {
            'status': -1,
            'error': 'Not Authorized',
            'data': None
        }

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
            'error':None,
            'data':ret_data
        }



# promo == * => lobby

def getCorrespondingChat(currentID):
    sql_cursor.execute(f'select * from users where id={currentID} ')
    user = sql_cursor.fetchone()
    if(user.promo=='*' and (not user.groupe=='*')) :
        return {
            'status': -2,
            'error': 'Invalid ChatRoom',
            'data': None
        }
    if(not validCurrentId(currentID)):
        return {
            'status':-1,
            'error':'Not Authorized',
            'data':None
        }

    chatrooms = mongo['bddd']['chatrooms']
    result = chatrooms.find({'promo':user.promo,'groupe':user.groupe})

    pass



def getCorrespondingMessages(currentID,promo,groupe,setNewMessages):
    if(not validCurrentId(currentID)): return

    chatRooms = mongo['bddd']['chatrooms']
    messages = mongo['bddd']['messages']
    chatRoom = chatRooms.find_one({'promo':promo,'groupe':groupe})
    with chatRoom.watch() as stream :
        for change in stream:
            print('Change detected:', change)
            setNewMessages(change)


    pass


def sendMessage(currentUser,chatID,promo,groupe,message):
    db = mongo['bddd']
    chatRooms = db['chatrooms']
    messages = db['messages']
    msg = messages.insert_one(message)
    result = chatRooms.update_one({'promo':promo,'groupe':groupe},{'$push':{'messages':msg.inserted_id}})

    pass