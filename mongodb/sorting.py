from connection import mycollection

result = mycollection.find({}).sort("price", -1)
result = mycollection.find({}).sort([("price", -1), ("name", 1)])

for i in result:
    print(i)
