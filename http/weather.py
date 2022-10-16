import requests

apiKey = "48b065b7df4e4f918b6200101220308"
url = "https://api.weatherapi.com/v1/current.json"

res = requests.get(url, params={
	"key": apiKey,
	"q": "Tovuz",
	"lang": "tr"

})

print(res.json())
