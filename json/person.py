import json

import requests

res = requests.get("https://jsonplaceholder.typicode.com/posts").json()

with open("person.json", "w") as file:
	json.dump(res, file)

print(type(res))
