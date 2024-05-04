import mysql.connector as connector
import pymongo
import bcrypt
from pymongo.server_api import ServerApi

bcrypt_secret = b's$cret12oaisjdpqhd-9jawpj-9qjd-19h2eh0q9jd-192jd-asjcpospchz0xinczmcpomas-djqw-9r-qhtsdnfajsf0ashgi0ewhc8ym8tcna90nchf90a'

salt = bcrypt.gensalt()


connection  = connector.connect(
user='achref', password='password',host='127.0.0.1',database='bddd',autocommit=True
)
#
connection  = connector.connect(
    host="monorail.proxy.rlwy.net",
    user="root",
    password="EfSYqdABwcnRZMlenSDeXHQHgkjGYofR",
    port="52256",
    database="railway",
    autocommit=True
)



sql_cursor = connection.cursor()


# mongo = pymongo.mongo_client.MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))
# sql_cursor.execute('create database bddd;')

# sql_cursor.execute('''
#     drop table if exists users;
# ''')
#
# sql_cursor.execute('''create table users (
#                     id  int auto_increment Primary Key,
#                     first_name varchar(64) not null,
#                     last_name varchar(64) not null,
#                     hashed_password varchar(255) not null,
#                     role varchar(32) not null,
#                     email varchar(64) unique,
#                     username varchar(64) unique,
#                     promo varchar(8),
#                     groupe varchar(2) ,
#                     profile_pic LONGBLOB
#                    )''')

#
sql_cursor.execute("insert into users (first_name,last_name,hashed_password,role,email,username,promo,groupe) values('admin' ,'admin' , '$2b$12$9im9zpxLp35Iw4FGKDXCqe2QXCgPocTO3qjG7F/67eA2gNKEdxmcS' , 'admin','admin@gmail.com','admin999' ,'2cs' ,'1' )")

sql_cursor.execute('select * from users')
print(sql_cursor.fetchall())


