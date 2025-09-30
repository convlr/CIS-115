# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 9/25/25
# PROGRAM: Programming Lab 5, Part 1
# PURPOSE: Ask the user to enter their number grade and display the
#          letter grade.
# =================================================================

# Get the user input
number = int(input("Enter your grade (0-100): "))  # need to close ()'s

# Determine the letter grade
if number >= 92:
    print("Your letter grade is an A!")
elif number >= 84:  # need to add : to end of statement
    print("Your letter grade is a B.")
elif number >= 76:
    print("Your letter grade is a C.")
elif number >= 68:  # wrong symbol we flip to greater than
    print("Your letter grade is a D.")
else:
    print("Your letter grade is an F.")
