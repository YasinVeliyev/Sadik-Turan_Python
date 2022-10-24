from connection import mycollection

product = {"name": "Samsung S5", "price": 2000}
result = mycollection.insert_one(product)
products = [{"name": "Samsung S6", "price": 3000}, {"name": "Samsung S10", "price": 7000},
            {"name": "Samsung S7", "price": 4000}, {"name": "Samsung S11", "price": 8000},
            {"name": "Samsung S8", "price": 5000}, {"name": "Samsung S12", "price": 9000},
            {"name": "Samsung S9", "price": 6000}, {"name": "Samsung S13", "price": 10000}]

result = mycollection.insert_many(products)
print(result)
