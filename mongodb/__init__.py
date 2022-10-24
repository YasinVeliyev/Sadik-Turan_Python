import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["node-app"]
mycollection = mydb["products"]
