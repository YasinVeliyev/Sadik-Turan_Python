from connection import mydb, mycursor


def insertProduct(urunler: list):
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
    sql = "SELECT COUNT(*) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT AVG(price) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT SUM(price) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT MAX(price) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT MIN(price) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT MIN(price) FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    sql = "SELECT name FROM products WHERE price=(SELECT MAX(price) from products)"

    mycursor.execute(sql)
    products = mycursor.fetchone()
    print(products)


get_products()
