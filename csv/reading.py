import csv

with open("bestsellers with categories.csv", encoding="utf8") as file:
	csv_reader = csv.reader(file)
	with open("books.csv", "w", encoding="utf8") as f:
		csv_writer = csv.writer(f)
		for i in csv_reader:
			csv_writer.writerow(i)
