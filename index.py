import mysql.connector
from mysql.connector import errorcode

try:
    cnn = mysql.connector.connect(
        user='u1034599',
        password='HG_tkjh9',
        host='localhost',
        database='miamorstore')
    print("It works!")
except mysql.connectorErrors as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("DataBase does not exist")
    else:
        print(e)

cursor = cnn.cursor()

addName = ("INSERT INTO Name (fName, lName) VALUES (%s, %s)")
fName = "Max"
lName = "Opanasenko"
empName = (fName, lName)

cursor.execute(addName, empName)

cnn.commit()
cursor.close()
cnn.close()