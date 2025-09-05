## Chapter 2 examples
#
## this is a single line comment
#
## this is a
## multi-line
## comment
#
#"""This is a multi-line
#comment
#"""
#
## print using a single string argument
#print("Hello, World!")  # this is an end-line comment
#
## printing a single number
#print(5)
#
## print multiple numbers
#print(1, 3, 5, 7, 9)
#
## create a multi-line string as a argument
#grading_scale = """A = 90-100
#B = 80-89
#C = 70-79
#D = 60-69
#F <= 59"""
## pass a variable as an argument
#print(grading_scale)
#
## print an empty line for spacing
#print()
#
## converting data types
#int1 = 50
#float1 = float(int1)
#print(int1, "cast as a float is:", float1)
#print("the type of float1 should be float:", type(float1))
#
#print()
## getting input for the user
#user_name = input("enter your name: ")
#print("Hello,", user_name)
#print("the data type of the input is:", type(user_name))
#print()

# get a numeric input from the user
#num = input("Enter a number: ")
#print("The number from the input is:", num)
#print("The data type of the inpuyt is:", type(num))
#print()
#num = int(input("Enter a number: "))
#print("The number from the input is:", num)
#print("The data type of the inpuyt is:", type(num))
#print()
#num = float(input("Enter a number: "))
#print("The number from the input is:", num)
#print("The data type of the inpuyt is:", type(num))
#print()

# mathematical operations
# floating point division
num = 9 / 4
print('9 / 4 =', num) # result in a floating point number 2.25
# truncated integer division
num = 9 // 4
print('9 // 4 =', num) # result in a integer 2
# dividing with a negative value
num = -9 // 4
print('-9 // 4 =', num) # value is truncated and will be -3

# other mathematical operators
num1 = 2
num2 = 3
print(num1, "+" , num2, "=", num1 + num2)
print(num2, "-" , num1, "=", num2 - num1)
print(num1, "*" , num2, "=", num1 * num2)
print(num1, "/" , num2, "=", num1 / num2)
print(num2, "//" , num1, "=", num2 // num1)
print(num1, "%" , num1, "=",4 % num1)
print(num1, "**" , num2, "=", num1 ** num2)

# mathematical operations with PEMDAS
print("The result of (4 + 2) / 3 + 4 =", (4 + 2) / 3 + 4) # results in a float
