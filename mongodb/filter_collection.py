from bson.objectid import ObjectId

from connection import mycollection

filter = {"name": "Samsung S5"}

result = mycollection.find_one(filter)
filter = {"_id": ObjectId("635440dc2bd898fe78218590")}
result = mycollection.find_one(filter)
result = mycollection.find({
    "name": {"$in": ["Samsing S5", "Samsung S6"]}
})

result = mycollection.find({
    "price": {"$gt": 5000}
})

result = mycollection.find({
    "price": {"$eq": 5000}
})

result = mycollection.find({
    "name": {"$regex": "S7$"}
})

print(*result)
