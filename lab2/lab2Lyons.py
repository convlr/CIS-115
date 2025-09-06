# ========================================
# NAME: your name goes here
# DATE: due date of the lab
# COURSE: CIS-115-your section number
# PURPOSE: The goal of this program is ...
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

