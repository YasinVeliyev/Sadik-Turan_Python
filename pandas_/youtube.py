import pandas as pd

df = pd.read_csv("./datasets/youtube-ing.csv")

result = df
result = len(df.columns)
result = df.head(20).tail(10)
result = df[10:20]
df.drop(["thumbnail_link", "description", "video_error_or_removed", "comments_disabled", "ratings_disabled"],
        inplace=True, axis=1)
result = df.head(100).mean()[["likes", "dislikes"]]
result = df[df["views"] == df["views"].max()]
result = df[df["views"] == df["views"].min()]
result = df.sort_values(by="views").tail(10)
df["title_len"] = df["title"].apply(len)
result = df['title_len']

df["tag_count"] = df["tags"].apply(lambda tags: len(tags.split("|")))

like_lists = list(df["likes"])
dislike_lists = list(df["dislike"])
result = df
print(result)
