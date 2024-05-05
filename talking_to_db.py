import mysql.connector as connector
import pymongo
import bcrypt
from pymongo.server_api import ServerApi
# import motor

bcrypt_secret = b's$cret12oaisjdpqhd-9jawpj-9qjd-19h2eh0q9jd-192jd-asjcpospchz0xinczmcpomas-djqw-9r-qhtsdnfajsf0ashgi0ewhc8ym8tcna90nchf90a'

salt = bcrypt.gensalt()

#
connection  = connector.connect(
    host="monorail.proxy.rlwy.net",
    user="root",
    password="EfSYqdABwcnRZMlenSDeXHQHgkjGYofR",
    port="52256",
    database="railway",
    autocommit=True
)


#
# connection = connector.connect(
# user='achref', password='password',host='127.0.0.1',database='bddd'
# )
# print(connection)

sql_cursor = connection.cursor()

mongo = pymongo.mongo_client.MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))

# print(mongo['bddd'])
db = mongo['bddd']
chatrooms = db['chatrooms']
# print(chatrooms)

print(chatrooms.find())