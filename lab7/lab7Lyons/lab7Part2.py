# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 10/15/25
# PROGRAM: Programming Lab 7, Part 2
# PURPOSE: This program takes a number from the user and multiplies
#          it by the numbers 1 - 5. It will then display a table
#          showing the values multiplied, the product, and whether
#          it is even or odd. The program continues to let the player
#          enter a new integer to multiply until they enter the
#          sentinel value, 999.
# =================================================================

# print the program purpose for the user
print("This program takes an integer number and multiplies it by the numbers 1 - 5.\nThen, it will display the results and if the product is even or odd.")

# set sentinel
cancel = 999

# priming read
int1 = int(input("Enter an integer number (999 to quit): "))

# loop if value is not the sentinel
while int1 != cancel:

    # print the display header
    print(f"{'value':<8}{'index':<8}{'product':<8}{'result':<8}")

    # loop from 1 to 5 inclusive
    for i in range(1, 6):

        # determine the product
        product = i * int1

        # if the product is even, set the result to even, else set it to odd
        if product % 2 == 0:
            result = "even"
        else:
            result = "odd"

        # print the output in order of value, index, product, and result
        print(f"{int1:<8}{i:<8}{product:<8}{result:<8}")

    # get a new value from the user
    int1 = int(input("Enter an integer number (999 to quit): "))
