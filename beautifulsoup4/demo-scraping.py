import csv
import json

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.sadikturan.com/")

obj = BeautifulSoup(res.text, "html.parser")
kurslar = obj.find_all(class_="card kurs")

with open("kurslar.csv", "w", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(["kurs_resmi", "kurs_baslik", "kurs_açıqlama", "udemy_link", "sayt_link"])

    for kurs in kurslar:
        kurs_resmi = kurs.find("img.jpeg")['src']
        kurs_baslik = kurs.find("h2").string
        kurs_açıqlama = kurs.find("span").string
        udemy_link = kurs.find(class_="card-footer").find_all("div")[1].find_all("a")[0]['href']
        sayt_link = f'https://www.sadikturan.com{kurs.find(class_="card-footer").find_all("div")[1].find_all("a")[1]["href"]}'
        writer.writerow([kurs_resmi, kurs_baslik, kurs_açıqlama, udemy_link, sayt_link])

with (open("kurslar.csv", "r", encoding="utf8") as csv_file, open("kurslar.json", "w") as json_file):
    reader = csv.DictReader(csv_file)
    json.dump(list(reader), json_file)
