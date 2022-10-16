import requests
from bs4 import BeautifulSoup

res = requests.get("https://web.telegram.org/k/#@python101az")

obj = BeautifulSoup(res.text, "html.parser")
divs = obj.find_all("div")
print(divs[0].attrs)
