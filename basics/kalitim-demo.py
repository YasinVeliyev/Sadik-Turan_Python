class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Şu anda aktif {cls.active_users} user var"

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Moderator(User):
    active_moderators = 0

    def __init__(self, firstname, lastname, community):
        super(Moderator, self).__init__(firstname, lastname)
        self.community = community
        Moderator.active_moderators += 1


u = User("Asim", "Veliyev")
m = Moderator("Yasin", "Veliyev", "Aze")

print(m.active_users)
print(m.display_active_users())
print(User.display_active_users())
