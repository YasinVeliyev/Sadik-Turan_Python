#
# data = [{
# 	"username": "Yasin Vəliyev",
# 	"firstname": "Yasin",
# 	"lastname": "Vəliyev"
# }, {
# 	"username": "Yasin Vəliyev",
# 	"firstname": "Yasin",
# 	"lastname": "Vəliyev"
# }, {
# 	"username": "Yasin Vəliyev",
# 	"firstname": "Yasin",
# 	"lastname": "Vəliyev"
# }, {
# 	"username": "Yasin Vəliyev",
# 	"firstname": "Yasin",
# 	"lastname": "Vəliyev"
# }]
#
# # with open("users.json", "w", encoding="utf8") as file:
# # 	json.dump(data, file, ensure_ascii=False, indent=2)
# user = {
# 	"id": 1,
# 	"username": "Yasin Vəliyev",
# 	"firstname": "Yasin",
# 	"lastname": "Vəliyev"
#
# }
#
# with open("users.json", "r", encoding="utf8") as file:
# 	users = json.load(file)
# users.append(user)
# with open("users.json", "w", encoding="utf8") as file:
# 	json.dump(users, file, ensure_ascii=False, indent=2)


# data = {
# 	"sadikturan": {
# 		"firstname": "Sadik",
# 		"lastname": "Turan"
# 	},
# 	"yasinveliyev": {
# 		"firstname": "Yasin",
# 		"lastname": "Veliyev"
# 	}
# }
# with open("users2.json", "w", encoding="utf8") as file:
# 	json.dump(data, file)

# class Product:
# 	def __init__(self, name, price):
# 		self.name = name
# 		self.price = price
#
#
# p1 = Product("Samsung S10", 5000)
import json
import os


class User:
	def __init__(self, username: str, password: str, email: str):
		self.email = email
		self.username = username
		self.password = password


class UserRepository:
	def __init__(self):
		self.users = []
		self.is_logged_in = False
		self.current_user = {}
		self.load_user()
		print(self.users)

	def load_user(self):
		if os.path.exists("users.json"):
			with open("users.json", "r", encoding="utf8") as file:
				users = json.load(file)
				self.users = users

	# for user in users:
	# 	new_user = User(email=user["email"], username=user["username"], password=user["password"])
	# 	self.users.append(new_user.__dict__)

	def register(self, user: User):
		self.users.append(user.__dict__)
		self.save_to_file()
		print("Kullanici olusturuldu")

	def login(self, username, password):
		for user in self.users:
			if user["username"] == username and user["password"] == password:
				self.is_logged_in = True
				self.current_user = user
				print("Login Yapildi")
				break
		pass

	def logout(self):
		self.is_logged_in = False
		self.current_user = {}
		print("Cikis Yapilde")

	def identity(self):
		if self.is_logged_in:
			print(f"Username: {self.current_user['username']}")
		else:
			print("Giri. yapilmadi")

	def save_to_file(self):
		with open("users.json", "w", encoding="utf8") as file:
			json.dump(self.users, file)


repository = UserRepository()
print(repository.users)
while True:
	print("Menu".center(50, "="))
	secim = input("""
1-Register
2-Login
3-Logout
4-Identity
5-Exit
""")
	match secim:
		case "1":
			username = input("Enter Username: ")
			password = input("Enter Password: ")
			email = input("Enter Email: ")
			user = User(username, password, email)
			repository.register(user)
		case "2":
			username = input("Enter Username: ")
			password = input("Enter Password: ")
			repository.login(username=username, password=password)
		case "3":
			repository.logout()
		case "4":
			repository.identity()
		case "5":
			break
		case other:
			print("Yanlış Seçim", other)

with open("urunler.json", "w", encoding="utf8") as file:
	pass
