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
# connection  = connector.connect(
# user='achref', password='password',host='127.0.0.1',database='bddd'
# )

print(connection)
sql_cursor = connection.cursor()


sql_cursor.execute('select * from users')
print(sql_cursor.fetchall())