# ========================================
# NAME: Brantley Lyons
# DATE: 9/7/25
# COURSE: CIS-115-NLE01
# PURPOSE: Completing Lab 2
# ========================================

# Problem 1: counting the powers of 2

print(2**0)
print(2**1)
print(2**2)
print(2**3)
print(2**4)
print(2**5)
print(2**6)
print(2**7)

# Problem 2: some user int rasied to the power of 2

userNumber = int(input("What power of two?: "))
squared = userNumber ** 2
print(f"Two to the power of {userNumber} is {squared}")

# Problem 3: user int raised to user int

base = int(input("What base?: "))
exponent = int(input(f"What power of {base}?: "))
powerResult = (base) ** exponent
print(f"{base} to the power of {exponent} is {powerResult}")

# Problem 4: convert user input to binary

d1 = int(input("Enter the leftmost digit: "))
d2 = int(input("Enter the next digit: "))
d3 = int(input("Enter the next digit: "))
d4 = int(input("Enter the next digit: "))

result = d1*8 + d2*4 + d3*2 + d4*1

print("The value is", result)

# Problem 5: convert decimal to binary

number = 13
print("The number I chose was 13")
print("13 in binary, with the digits in reverse order is:")
remainder = number % 2
number = number // 2
print(remainder)
remainder = number % 2
number = number // 2
print(remainder)
remainder = number % 2
number = number // 2
print(remainder)
remainder = number % 2
number = number // 2
print(remainder)
remainder = number % 2
number = number // 2
print(remainder)

# Problem 6: dividing user ints

digit1 = int(input("Enter your first number: "))
digit2 = int(input("Enter your second number: ")) 
division = digit1 / digit2
print(f"{division:.3f}")  # formatting to 3 decimal places

# Problem 7: dividing user floats

float1 = float(input("Enter a floating-point value: "))
float2 = float(input("Enter second floating-point: "))
dividing = float1 / float2
print(f"{dividing:.5f}")  # formatting again

# Problem 8: dividing user floats and displaying in scientific notation

floatingPoint1 = float(input("Enter a floating-point value: "))
floatingPoint2 = float(input("Enter second floating-point: "))
divideFloats = floatingPoint1 / floatingPoint2
print(f"{divideFloats:.6e}")  # e to format in scientific notation

# Problem 9: display two user ints into each arithmetic equation

userInt1 = int(input("Enter first number: "))
userInt2 = int(input("Enter second number: "))
print(userInt1, "+" , userInt2, "=", userInt1 + userInt2)
print(userInt1, "-" , userInt2, "=", userInt1 - userInt2)
print(userInt1, "*" , userInt2, "=", userInt1 * userInt2)
print(f"{userInt1} /  {userInt2} = {userInt1 / userInt2:.2f}")
print(userInt1, "//" , userInt2, "=", userInt1 // userInt2)
print(userInt1, "%" , userInt2, "=", userInt1 % userInt2)
print(f"{userInt1} ** {userInt2} = {userInt1 ** userInt2:,}")
