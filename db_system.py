import mariadb
import sys

# Connect to MariaDB Platform
def config():
    
    conn = mariadb.connect(
	user="sa",
	password="volt2",
	host="127.0.0.1",
	port=3306,
	database="db_volt"
    )

# Get Cursor
    cur = conn
    return cur

def get_databases():
    result = ""
    curs = config()
    cur = curs.cursor()
    cur.execute("SHOW DATABASES")
    result = cur.fetchall()
    database = listToString(result[0])
    if database == "db_volt":
        result = 'connected'
    else:
        result = 'failed'
    print(result)
    return result

def get_data(sqlquery):
    query = sqlquery
    result = ""
    curs = config()
    cur = curs.cursor()
    cur.execute(query)
    result = cur.fetchall()
    #data = ",".join(map(str, result)) 
    for x in result:
       return listToString(x) 

def listToString(s):
    str1 = " "
    return(str1.join(s))

def convertTuple(tup):
    str = ''.join(tup)
    return str

    
if __name__ == "__main__":
    get_data("Select Password From users")
