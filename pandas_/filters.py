import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
result = df.columns
result = df.head(10)
result = df.tail()
result = df["Column1"].head()
result = df[["Column1", "Column2"]].head()

result = df[df["Column1"] > 50][["Column1", "Column2"]]

result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]["Column1"]
result = df[(df["Column1"] > 50) & (df["Column2"] > 70)][["Column1", "Column2"]]
result = df.query("Column1>=50 & Column2>=50")[["Column1", "Column2"]]
print(result)
