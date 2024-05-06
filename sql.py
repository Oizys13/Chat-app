import mysql.connector as sql_cn

#function 1 :creates a connection with mysql database and return the connection object

def create_connection(host,user,pswd, db,port):
   connection = sql_cn.connect(
		host=host,
		user=user,
		password=pswd,
        port=port,
		database = db)
   return connection

	


# function 2 :execute_query(query, connection): -> list of results or empty list 


def execute_query(query,params, connection):
	cursor = connection.cursor(buffered=True)
	cursor.execute(query,params)
	connection.commit()
	results = cursor.fetchall()
	return results
 

#function 3 :
def close_connection(connection): 
   connection.close()