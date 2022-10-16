from connection import mydb, mycursor


def insertProduct(urunler: list):
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
if __name__ == "__main__":
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
