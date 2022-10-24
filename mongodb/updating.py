from connection import mycollection

result = mycollection.update_one({"name": "Samsung S5"}, {"$set": {"price": 2500}})
result = mycollection.update_one({"name": "Samsung S13"}, {"$set": {"name": "Nokia G20"}})

result = mycollection.find_one({"name": "Nokia G20"})
print(result)
