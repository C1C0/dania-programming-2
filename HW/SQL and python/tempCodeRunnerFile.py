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

DB_TABLE_CUSTOMERS = 'customers'
cursor.execute(f"USE {DB_NAME}")
cursor.execute(f"DROP TABLE IF EXISTS {DB_TABLE_CUSTOMERS}")
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {DB_TABLE_CUSTOMERS} (name VARCHAR(255), address VARCHAR(255));")
# cursor.execute("SHOW TABLES")

cursor.execute(f"""INSERT INTO {DB_TABLE_CUSTOMERS} (name, address) VALUES (%s, %s);""", ("User 1", "Address 1"))

# cursor.executemany(f"""
# INSERT INTO `{DB_TABLE_CUSTOMERS}` (`name`, `address`)
# VALUES (%s, %s)
# """, [
#     ("User 1", "Address 1"),
#     ("User 2", "Address 2"),
#     ("User 3", "Address 3"),
#     ("User 4", "Address 4"),
# ])

con.close()
