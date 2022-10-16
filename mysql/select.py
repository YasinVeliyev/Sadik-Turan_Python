import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("/home/yasin/Udemy/SadikTuranPython/.env")
mydb = mysql.connector.connect(host="localhost", user="yasinv", password=os.environ.get("DB_PASSWORD"),
                               database="node-app", auth_plugin='mysql_native_password')


def insertProduct(urunler: list):
    mycursor = mydb.cursor()
    sql = """INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s);"""
    mycursor.executemany(sql, urunler)
    try:
        mydb.commit()
        print(f"{mycursor.lastrowid}")
        print(f"{mycursor.rowcount}")
    except Exception as err:
        print(err)
    finally:
        mydb.close()


def get_products():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    print(products)


get_products()
