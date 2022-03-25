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
)""")

cursor.execute(f"DROP TABLE IF EXISTS `{DB.TABLE2}`")
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS `{DB.TABLE2}` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255),
    `subject` VARCHAR(255),
    PRIMARY KEY (`id`)
)""")

con.close()