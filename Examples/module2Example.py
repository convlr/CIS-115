#### Chapter 2 examples
###
#### this is a single line comment
###
#### this is a
#### multi-line
#### comment
###
###"""This is a multi-line
###comment
###"""
###
#### print using a single string argument
###print("Hello, World!")  # this is an end-line comment
###
#### printing a single number
###print(5)
###
#### print multiple numbers
###print(1, 3, 5, 7, 9)
###
#### create a multi-line string as a argument
###grading_scale = """A = 90-100
###B = 80-89
###C = 70-79
###D = 60-69
###F <= 59"""
#### pass a variable as an argument
###print(grading_scale)
###
#### print an empty line for spacing
###print()
###
#### converting data types
###int1 = 50
###float1 = float(int1)
###print(int1, "cast as a float is:", float1)
###print("the type of float1 should be float:", type(float1))
###
###print()
#### getting input for the user
###user_name = input("enter your name: ")
###print("Hello,", user_name)
###print("the data type of the input is:", type(user_name))
###print()
##
### get a numeric input from the user
###num = input("Enter a number: ")
###print("The number from the input is:", num)
###print("The data type of the inpuyt is:", type(num))
###print()
###num = int(input("Enter a number: "))
###print("The number from the input is:", num)
###print("The data type of the inpuyt is:", type(num))
###print()
###num = float(input("Enter a number: "))
###print("The number from the input is:", num)
###print("The data type of the inpuyt is:", type(num))
###print()
##
### mathematical operations
### floating point division
##num = 9 / 4
##print('9 / 4 =', num) # result in a floating point number 2.25
### truncated integer division
##num = 9 // 4
##print('9 // 4 =', num) # result in a integer 2
### dividing with a negative value
##num = -9 // 4
##print('-9 // 4 =', num) # value is truncated and will be -3
##
### other mathematical operators
##num1 = 2
##num2 = 3
##print(num1, "+" , num2, "=", num1 + num2)
##print(num2, "-" , num1, "=", num2 - num1)
##print(num1, "*" , num2, "=", num1 * num2)
##print(num1, "/" , num2, "=", num1 / num2)
##print(num2, "//" , num1, "=", num2 // num1)
##print(num1, "%" , num1, "=",4 % num1)
##print(num1, "**" , num2, "=", num1 ** num2)
##
### mathematical operations with PEMDAS
##print("The result of (4 + 2) / 3 + 4 =", (4 + 2) / 3 + 4) # results in a float
##
### breaking up a statement onto a second line
##result = (4 + 2) / 3 \
##         + 4
##print("Still works! The result of (4 + 2) / 3 + 4 =", result)
##print()
##
## using string formatting to format output
## using the flowchart example
#hours_worked = float(input("Enter number of hours worked: "))  # casting the
#hourly_pay_rate = float(input("Enter the hourly pay rate: "))
## calculate gross pay
#gross_pay = hours_worked * hourly_pay_rate
## use an f-string to format
#print(f"The gross pay is: ${gross_pay:.2f}")
#
#print()
## create
#quotes1 = 'I can use "quotes" as '
#quotes2 = """I can use "quotes" and 'quotes'"""
#print(quotes1)
#print(quotes2)
#print()
#
## string concatenation
## usinc numeric values (int/float), we must cast to a string
#print("Using string conatenation. The result of (4 + 2) / 3 + 4 =", + str(result))

# inplicit string concatenation
result = 'one' 'two' 'three'
print(result)

# we can override the default ending behavior
print(num1, end=' -> ')  # stay on same line
print(num2)  # uses default ending so will go to the next line

# special characters in the print function
print("Here is a string using a newline character and tab\n\t"
        "using common special character and adding an extra line at the end.\n")

INTEREST_RATE = 0.2
value = 100 * INTEREST_RATE
print(f"The value based on the interest rate is: ${INTEREST_RATE:,.2f}")

