# ==============================================
# NAME: Brantley Lyons
# DATE: 9/24/2025
# COURSE: CIS-115-NLE01
# PURPOSE: Decision Structures and Boolean Logic
# ==============================================

# Problem 1: Practice using nested if statements
value = int(input("Enter the number of college credits earned: "))
if value > 90:
        print("Senior Status")
else:
        if value > 60:
                print("Junior Status")
        else:
                if value > 30:
                        print("Sophmore Status")
                else:
                        print("Freshman status")

# Problem 2: Practice using ELIF statements
credits = int(input("Enter the number of college credits earned: "))
if credits > 90:
        print("Senior Status")

elif credits > 60:
        print("Junior Status")

elif credits > 30:
        print("Sophmore Status")

else:
        print("Freshman Status")

# Problem 3: Practice using nested if statements
fruits = input("Enter 'A' for apple, 'B' for banana, or 'C' for coconut: ")
if fruits == "A" or fruits == "a":
        print("Apple")
else:
        if fruits == "B" or fruits == "b":
                print("Banana")
        else:
                if fruits == "C" or fruits == "c":
                        print("Coconut")
                else:
                        print("Invalid Input!")

# Problem 4: Practice using ELIF statements
fruits2 = input("Enter 'A' for apple, 'B' for banana, or 'C' for coconut: ")
if fruits2 == "A" or fruits2 == "a":
        print("Apple")

elif fruits2 == "B" or fruits2 == "b":
        print("Banana")

elif fruits2 == "C" or fruits2 == "c":
        print("Coconut")

else:
        print("Invalid Input!")

# Problem 5: Practice using if statements
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

s1_squared = round(side1 ** 2, 0)
s2_squared = round(side2 ** 2, 0)
s3_squared = round(side3 ** 2, 0)

is_equilateral = (side1 == side2) and (side2 == side3)

is_isosceles = (side1 == side2) or (side2 == side3) or (side1 == side3)

is_right = (s1_squared + s2_squared == s3_squared) or \
           (s2_squared + s3_squared == s1_squared) or \
           (s1_squared + s3_squared == s2_squared)

is_isosceles_right = is_isosceles and is_right

if is_equilateral:
    print("This is an Equilateral triangle!")

elif is_isosceles_right:
    print("This is an Isosceles Right triangle!")

elif is_isosceles:
    print("This is an Isosceles triangle!")

elif is_right:
    print("This is a Right triangle!")

else:
    print("This is a Scalene triangle!")
