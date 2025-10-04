# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 10/2/25
# PROGRAM: Programming Lab 6
# PURPOSE: Ask the user to enter their number grade and display the
#          letter grade.
# =================================================================

print("Problem 1: Practice using a for loop")
print("Adding up even numbers between 100 and 200, inclusive!")

total = 0
for i in range(100, 201, 2):
	total += i

print(total)

print("Problem 2: Practice using a while loop")
print("Adding up even numbers between 100 and 200, inclusive!")

something = 0
value = 100
while value <= 200:
	something += value
	value += 2

print(something)

print("Problem 3: Summing values entered by the user")

add = 0
while True:
	user_int = int(input("Enter a number (-1 to quit): "))
	if user_int == -1:
		break
	add += user_int

print(f"The sum is: {add}")

new_add = 0
first = True
while True:
	if first:
		user_num = int(input("Enter the first number to sum (-1 to quit): "))
		first = False
	else:
		user_num = int(input("Enter the next number (-1 to quit): "))
	if user_num == -1:
		break
	if 0 <= user_num <= 100:
		new_add += user_num

print(f"The sum of all the positive values less than 100 is: {new_add}")


