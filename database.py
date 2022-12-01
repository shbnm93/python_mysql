import mysql.connector

config = {
    'user' : 'root',
    'password' : '123456',
    'host' : 'localhost',
    'database' : 'acme'
}


db = mysql.connector.connect(**config)
cursor = db.cursor()