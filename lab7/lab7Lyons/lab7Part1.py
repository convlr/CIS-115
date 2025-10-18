#=================================================================
# AUTHOR: Brantley Lyons
# DATE: 10/15/25
# PROGRAM: Programming Lab 7, Part 1
# PURPOSE: Ask the user for two numbers, one is the value to multiply
#          by the loop index and the other is how many times to
#          perform it. Loop and display the multiplication results.
# =================================================================

# get the number from the user
number = int(input("Enter a number to multiply (1 - 100): "))

# validate user input for the number
while number < 1 or number > 100:  # wrong syntax
    number = int(input("Invalid input! Enter a number from 1 - 100: "))

# get the stop value from the user
end = int(input("Enter the stop value (1 - 10): "))

# validate user input for the stop value
while end < 1 or end > 10:  # logic error
    end = int(input("Invalid input! Enter a number from 1 - 10: "))

# set the index to 1 to start
index = 1

# loop while the index is less than or equal to end
while index <= end:

    # multiply and print
    product = number * index
    print(product)

    # increment the index value
    index += 1  # logic error
