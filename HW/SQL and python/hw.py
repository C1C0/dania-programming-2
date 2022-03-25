import mysql.connector as mysqlC
from mysql.connector.cursor import MySQLCursor
from config import MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER

con: mysqlC.MySQLConnection = mysqlC.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor: MySQLCursor = con.cursor()

DB_NAME = "pythondb"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

con.close()