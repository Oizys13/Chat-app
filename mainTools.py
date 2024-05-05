import sql
import hashlib
import mongo
from PIL import Image
import io
import bcrypt
connection = sql.create_connection(host="monorail.proxy.rlwy.net",
    user="root",
    pswd="EfSYqdABwcnRZMlenSDeXHQHgkjGYofR",
    port="52256",
    db="railway"
)
mondb = mongo.getDb()


def encode_password(password):
    # Convert password to bytes
    password_bytes = password.encode('utf-8')

    # Generate salt and hash the password
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    # Convert hashed password to string for storage
    hashed_password_str = hashed_password.decode('utf-8')

    return hashed_password_str


def check_password(password, hashed_password):
    # Convert password to bytes
    password_bytes = password.encode('utf-8')

    # Convert hashed password from string to bytes
    hashed_password_bytes = hashed_password.encode('utf-8')

    # Check if password matches hashed password
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


def authenticate(username, password):
    # connection = sql.create_connection()
    query = f"SELECT * FROM `users` u WHERE `username` = {username} "
    print(query)
    results = sql.execute_query(query, connection)[0]
    enc_psw = results[3]
    if check_password(password, enc_psw):
        return results, True, ''
    else:
        error = 'username or password is incorrect'
        return None, False, error


def get_users(usernames):
    if isinstance(usernames, tuple):
        query = f'''select * from users u where u.username in {str(usernames)}'''
    elif isinstance(usernames , str):
        query = f'''select * from users u where u.username = {str(usernames)}'''

    users = sql.execute_query(query, connection)
    return users



def get_chats(space, group, promo):
    collection = None
    query = {}
    if space == 'group':
        collection = mongo.get_collection('groups', mondb)
        query = {'group':group}

    elif space == 'promo':
        collection = mongo.get_collection('promos', mondb)
        query = {'promo':promo}

    elif space == 'all':
        collection = mongo.get_collection('all', mondb)
        query = {}

    chats = mongo.execute_query(collection, query)
    return chats


def add_message(message, document,  collection):
    filter_query = {'_id':document['_id']}
    update_query = {'$push':{'messages':message}}
    collection.update_one(filter_query, update_query)
    return collection.find_one(filter_query)


# def remove_message(messages, collection):
#     return mongo.remove_items(messages, collection)


def read_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    return image
