import mysql.connector

# function to connect with database

def databaseConnector():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythonDB"
    )
    return mydb

#databaseConnect()
