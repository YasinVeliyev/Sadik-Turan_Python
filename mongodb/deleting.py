from connection import mycollection

result = mycollection.delete_one({"name": "Nokia G20"})

print(result)
