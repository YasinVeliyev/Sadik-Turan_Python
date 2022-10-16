class Comment:
    def __init__(self, username: str, text: str, likes: int, dislikes: int):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self):
        return f"Comment(Username:{self.username}, Comment:{self.text}, Likes:{self.likes}, Dislikes:{self.dislikes})"


c1 = Comment("Yasin", "Hi", 5, 6)
c2 = Comment("Yasin", "Hi", 5, 6)
c3 = Comment("Yasin", "Hi", 5, 6)
c4 = Comment("Yasin", "Hi", 5, 6)
c5 = Comment("Yasin", "Hi", 5, 6)

for c in [c1, c2, c3, c4, c5]:
    print(c)
