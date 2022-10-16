import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("../../.env")

mydb = mysql.connector.connect(host="localhost", user="yasinv", password=os.environ.get("DB_PASSWORD"),
                               auth_plugin='mysql_native_password', database="node-app")
mycursor = mydb.cursor()

# mycursor.execute("""CREATE DATABASE IF NOT EXISTS mydatabase;""")
# db = mycursor.execute("SHOW DATABASES;")
# for i in mycursor:
#     print(i)
