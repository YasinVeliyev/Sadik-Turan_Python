import pandas as pd

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 45, 25],
    "Column3": ["abc", "bca", "ade", "cba", "dea"]
}
df = pd.DataFrame(data)
result = df
result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column2"].apply(lambda x: x ** 2)
result = df["Column3"].apply(lambda x: len(x))
print(result)
