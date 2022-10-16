from connection import mycursor


def get_products():
    sql = "SELECT * FROM products WHERE name LIKE '%Samsung%' ORDER BY id DESC"
    mycursor.execute(sql)
    products = mycursor.fetchall()
    print(products)


get_products()
