import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("/home/yasin/Udemy/SadikTuranPython/.env")


def insertProduct(urunler: list):
    mydb = mysql.connector.connect(host="localhost", user="yasinv", password=os.environ.get("DB_PASSOWRD"),
                                   auth_plugin='mysql_native_password', database="node-app")
    mycursor = mydb.cursor()
    mycursor.executemany("""INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s);""", urunler)
    try:
        mydb.commit()
        print(f"{mycursor.lastrowid}")
        print(f"{mycursor.rowcount}")
    except Exception as err:
        print(err)
    finally:
        mydb.close()


urunler = []
while True:
    name = input("Urun adi")
    price = float(input("Urun Fiyati"))
    imageUrl = input("Urun sekli")
    description = input("Urun hakkinda")
    result = input("Devam etmek istiyorsunuz? (e/h)")
    urunler.append((name, price, imageUrl, description))
    if result == 'e':
        continue
    else:
        insertProduct(urunler)
        break
