from connection import mydb, mycursor


def update_product(id, name, price):
    sql = "UPDATE products SET price=%s,name=%s where id=%s;"
    mycursor.execute(sql, (price, name, id))
    try:
        mydb.commit()
        print(f"{mycursor.lastrowid}")
        print(f"{mycursor.rowcount} tane kayit guncellendi")
    except Exception as err:
        print(err)
    finally:
        mydb.close()


update_product(1, "Iphone 8", 7000)
