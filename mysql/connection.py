import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("/home/yasin/Udemy/SadikTuranPython/.env")

mydb = mysql.connector.connect(host="localhost", user="yasinv", password=os.environ.get("DB_PASSOWRD"),
                               auth_plugin='mysql_native_password', database="mydatabase")
mycursor = mydb.cursor()

# mycursor.execute("""CREATE DATABASE IF NOT EXISTS mydatabase;""")
# db = mycursor.execute("SHOW DATABASES;")
# for i in mycursor:
#     print(i)


mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255), address VARCHAR(255));
""")
