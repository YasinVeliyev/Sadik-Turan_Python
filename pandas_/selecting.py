import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])

result = df
result = df[["Column1", "Column2"]]
# print(type(result))
result = df.loc["A"]
result = df.loc[:, "Column1"]
result = df.loc["A", "Column1":"Column3"]
result = df.iloc[[0, 2], [0, 1]]
df["Column4"] = pd.Series(np.random.randn(3), ["A", "B", "C"])
df["Column5"] = df["Column1"] + df["Column4"]
result = df.drop("Column5", axis=1, inplace=True)
print(df)
print(result)
