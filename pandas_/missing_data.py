import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=["a", "c", "e", "f", "h"], columns=["Column1", "Column2", "Column3"])
result = df

df = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
newColumn = [80, 30, 70, 51, np.nan, 30, np.nan, 10]
df["Column4"] = newColumn

result = result.drop("Column1", axis=1)
result = df.drop(["Column1", "Column2"], axis=1)
result = df.isnull().sum()
result = df.isnull()["Column1"].sum()
result = df["Column1"].isnull()
result = df[df["Column1"].isnull()]
result = df[df["Column1"].notnull()]
result = df.dropna()
result = df.dropna(how="all")
result = df.dropna(axis=1, how="any")

result = df.dropna(subset=["Column1", "Column2"], how="all")
result = df.dropna(thresh=2, subset=["Column1", "Column2"])
result = df.dropna(thresh=3, subset=["Column1", "Column2"])
print(df)
result = df.dropna(thresh=3, subset=["Column1", "Column2"])

result = df.fillna(value=0)


# print(result)


def ortalama(df):
    toplam = df.sum()
    adet = df.size - df.isnull().sum()
    return toplam / adet


result = df.fillna(value=ortalama(df))
print(result)
