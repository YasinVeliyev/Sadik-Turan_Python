import pandas as pd

df = pd.read_csv("./datasets/nba.csv")
result = df
result = df.head()
result = len(df)
result = len(df.index)
result = df.columns
result = df["Salary"].max()
result = df["Salary"].mean()
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team", "Age"]].sort_values(by="Age", ascending=False)
result = df[(df["Name"] == "John Holland")]["Team"]
result = df.groupby("Team")["Salary"].mean()
result = len(df.groupby("Team"))
result = df["Team"].nunique()
result = df["Team"].value_counts()
df.dropna(inplace=True)
result = df[df["Name"].str.contains("and")]


def str_find(name):
    if "and" in name.lower():
        return True
    return False


result = df[df["Name"].apply(str_find)]
result = df[df["Name"].apply(lambda string: "and" in string)]

print(result)
