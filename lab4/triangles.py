side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 == side3:
	print("This is an Equilateral triangle!")

elif (side1 == side2 or side2 == side3 or side1 == side3) and (round(side1**2 + side2**2, 0) == round(side3**2, 0)) or \
	(round(side2**2 + side3**2, 0) == round(side1**2, 0)) or \
	(round(side1**2 + side3**2, 0) == round(side2**2, 0)):
	print("This is an Isosceles Right triangle!")

elif side1 == side2 or side2 == side3 or side1 == side3:
	print("This is an Isoscele trinagle!")

elif round(side1**2 + side2**2, 0) == round(side3**2, 0):
	print("This is a Right triangle!")

else:
	print("This is a Scalene triangle!")
