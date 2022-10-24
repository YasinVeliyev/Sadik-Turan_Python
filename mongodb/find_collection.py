from connection import mycollection

result = mycollection.find_one({"name": "Samsung S5"})
result = mycollection.find({"name": "Samsung S7"}, {"name": 1, "_id": 0})

print(*result)
