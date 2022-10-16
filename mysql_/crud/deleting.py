from connection import mydb, mycursor


def delete_product(id):
    sql = "DELETE FROM products WHERE id=%s;"
    mycursor.execute(sql, (id,))
    try:
        mydb.commit()
        print(f"{mycursor.lastrowid}")
        print(f"{mycursor.rowcount} tane kayit silindi")
    except Exception as err:
        print(err)
    finally:
        mydb.close()


delete_product(2)
