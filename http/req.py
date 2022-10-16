import requests

res = requests.get("https://jsonplaceholder.typicode.com/todos?id=1")
sonuc = res.json()
print(sonuc)
