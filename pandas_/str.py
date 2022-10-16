import pandas as pd

data = pd.read_csv("./datasets/nba.csv")

result = data
result = data.dropna()
result = result.columns
data["player_name"] = data["player_name"].str.upper()
result = data
data["index"] = data["player_name"].str.find("A")
result = data[data.player_name.str.contains("JORDAN")]
# data[["Firstname", "Lastname"]] =
data[["Firstname", "Lastname"]] = data["player_name"].loc[data["player_name"].str.split().str.len() == 2].str.split(
    expand=True)
print(result)
