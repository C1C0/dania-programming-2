from hashlib import new
from operator import ne
import mysql.connector as mysqlC
from mysql.connector.cursor import MySQLCursor
from config import MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER
from db import DB

con: mysqlC.MySQLConnection = mysqlC.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor: MySQLCursor = con.cursor()

# 1
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB.NAME}")
cursor.execute(f"USE {DB.NAME}")

# 2
cursor.execute(f"DROP TABLE IF EXISTS `{DB.TABLE1}`")
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS `{DB.TABLE1}` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255),
    `subject` VARCHAR(255),
    PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=1""")

cursor.execute(f"DROP TABLE IF EXISTS `{DB.TABLE2}`")
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS `{DB.TABLE2}` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255),
    `subject` VARCHAR(255),
    PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=1""")

# 3
cursor.executemany(f"""
INSERT INTO `{DB.TABLE2}` (`name`, `subject`)
VALUES (%s, %s)
""", [
    ("Roman", "Python"),
    ("Patrik", "Networking"),
])

cursor.executemany(f"""
INSERT INTO `{DB.TABLE1}` (`name`, `subject`)
VALUES (%s, %s)
""", [
    ("Sami", "Python"),
    ("Mads", "Networking"),
])

con.commit()
cursor.execute(f"SELECT * FROM {DB.TABLE1}")

print("Table:", DB.TABLE1)
for x in cursor:
    print(x)

cursor.execute(f"SELECT * FROM {DB.TABLE2}")

print("Table:", DB.TABLE2)
for x in cursor:
    print(x)

# 4
newName = "ItStudents"
cursor.execute(f"DROP TABLE IF EXISTS {newName}")
cursor.execute(f"ALTER TABLE {DB.TABLE2} RENAME TO {newName}")
DB.TABLE2 = newName

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)
    
# 5
cursor.execute(f"""
INSERT INTO `{DB.TABLE2}` (`name`, `subject`)
VALUES (%s, %s)
""", ("Radek", "Python"))

# 6
cursor.execute(f"""
UPDATE `{DB.TABLE1}`
SET subject=%s
WHERE id=%s
""", ("Networking", 1))

con.commit()

# 7
con.autocommit = True
cursor.execute(f"""
DELETE FROM `{DB.TABLE2}`
WHERE id=%s
""", (2,))

# 8
cursor.execute(f"SELECT * FROM {DB.TABLE2} WHERE subject='Networking'")
print("ONLY NETWORKING STUDENTS")
for x in cursor:
    print(x)
    

con.close()