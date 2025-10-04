# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 10/2/25
# PROGRAM: Programming Lab 6
# PURPOSE: Practice with loops 
# =================================================================

# Problem 1
print("Problem 1: Practice using a for loop")
print("Adding up even numbers between 100 and 200, inclusive!")

total = 0
for i in range(100, 201, 2):
	total += i

print(f"{total}\n")

print("Problem 2: Practice using a while loop")
print("Adding up even numbers between 100 and 200, inclusive!")

# Problem 2
something = 0
value = 100
while value <= 200:
	something += value
	value += 2

print(f"{something}\n")

print("Problem 3: Summing values entered by the user")

# Problem 3
add = 0

while True:
	user_int = int(input("Enter a number (-1 to quit): "))
	if user_int == -1:
		break
	add += user_int

print(f"The sum is: {add}\n")

# Problem 4
print("Problem 4: Summing positive values entered by user that are less than 100")

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

print(f"The sum of all the positive values less than 100 is: {new_add}\n")

# Problem 5
print("Problem 5: Counting the number of positive and negative values entered by the user")

positive = 0
negative = 0
first_iteration = True

while True:
	if first_iteration:
		user_value = input("Enter the first number (enter q to quit): ")
		first_iteration = False
	else:
		user_value = input("Enter the next number (enter q to quit): ")

	if user_value == "q":
		break

	user_value = int(user_value)
	
	if user_value > 0:
		positive += 1
	elif user_value < 0:
		negative += 1

print(f"The number of positive values entered is: {positive}")
print(f"The number of negative values entered is: {negative}")
