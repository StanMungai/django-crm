import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Kangethe24'
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE IF NOT EXISTS crm")

print("All done!")