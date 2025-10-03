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

