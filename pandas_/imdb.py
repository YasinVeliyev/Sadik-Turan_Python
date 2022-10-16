import pandas as pd

df = pd.read_csv("./datasets/imdb.csv", encoding="utf8", encoding_errors="replace")

result = df

result = df.head(5)
result = df.tail()
result = df.tail(10)
print(result)
result = df.columns
result = df.head(10)
result = df["Title"]
result = result.head(5)
result = df[["Title", "Rated"]]
result = result.head()
result = df[["Title", "Rated"]].tail(7)
result = df[df["imdbRating"] >= 8][["Title", "imdbRating"]].head(50)
result = df[(df["Year"] >= 2014) & (df["Year"] <= 2015)]
result = result[["Title", "imdbRating"]].head(50)
result = df[((df["imdbRating"] >= 8) & (df["imdbRating"] <= 9)) & ((df["Year"] >= 2014) & (df["Year"] <= 2015))]

print(result[["Title", "Year", "imdbRating"]])
print(result.columns)
