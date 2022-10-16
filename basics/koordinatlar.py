import turtle

turtle.penup()
DMX = float(input("Dairənin mərkəzinin X koordinatını daxil edin: "))
DMY = float(input("Dairənin mərkəzinin Y koordinatını daxil edin: "))
D = float(input("Dairenin diametrini daxil edin: "))
R = D / 2
print(f"XMax={DMX + R} XMin={DMX - R}")
# Xmax = DMX + R
# Xmin = DMX-R
turtle.goto(DMX, DMY)
turtle.dot(D, 'green')
turtle.goto(0, 0)
while True:
	X = float(input("Nöqtənin X koordinatını daxil edin: "))
	YMin = DMY - pow(pow(R, 2) - pow(X - DMX, 2), 0.5)
	YMax = DMY + pow(pow(R, 2) - pow(X - DMX, 2), 0.5)
	print(f"YMax={YMax} YMin={YMin}")
	Y = float(input("Nöqtənin Y koordinatını daxil edin: "))
	turtle.goto(X, Y)
	turtle.dot(5, 'red')
	turtle.goto(0, 0)

turtle.exitonclick()
turtle.ev

a = [1, 2, 3, 4, 5, 6]
a.sort()
