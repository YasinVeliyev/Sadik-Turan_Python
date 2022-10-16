import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts",
                         data={"title": "deneme", "body": "deneme", "userId": 1})

print(response.json())
