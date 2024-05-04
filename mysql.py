# import mysql.connector as sql_cn

# #function 1 :creates a connection with mysql database and return the connection object

# def create_connection(host,user,pswd, db):
#    connection = sql_cn.connect(
# 		host=host,
# 		user=user,
# 		password=pswd,
# 		database = db)
#    return connection

	


# # function 2 :execute_query(query, connection): -> list of results or empty list 


# def execute_query(query, connection):
# 	cursor = connection.cursor()
# 	cursor.execute(query)
# 	connection.commit()
# 	results = cursor.fetchall()
# 	return results
 

# #function 3 :
# def close_connection(connection): 
#    connection.close()