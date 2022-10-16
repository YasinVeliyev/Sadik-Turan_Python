import requests

apiKey = "c9ed4d965e8c4f2397c534f2de5c2451"
response = requests.get("https://newsapi.org/v2/top-headlines", params={
	"apiKey": apiKey,
	"country": "tr",
	"sortBy": "publishedAt"
})

print(response.json())
