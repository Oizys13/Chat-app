from mysql.connector import connect
from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient




# sqlclient = connect(
#     host="monorail.proxy.rlwy.net",
#     user="root",
#     password="EfSYqdABwcnRZMlenSDeXHQHgkjGYofR",
#     port="52256",
#     database="railway"
# )
#
#
# cursor = sqlclient.cursor()
#
#
#
# print(cursor)
#
#
# sqlclient.close()



# mongo = MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))
# db = mongo['bddd']
# messages = db['messages']
# print(messages.find_one()['_id'])
#
# mongo.close()