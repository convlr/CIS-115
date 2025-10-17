# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 10/22/25
# PROGRAM: Programming Project 1, Part 1
# PURPOSE: This program will continually prompt the user for grades.
#          It will print out a letter grade each time the user enters
#          a number. The value must be within 1 - 100 and when the
#          user enters 999, the program stops prompting and will
#          print the user's average grade.
# =================================================================

# initialize count (0), total (0), and sentinel (999)
COUNT = 0
TOTAL = 0
STOP = 999

# create the priming read
# initialize number to an integer given by the user
user_num = int(input("Enter a number (1-100, 999 to quit): "))

# validate user input for the number (1 - 100, or 999)
# hint: this should use a while loop

while not (1 <= user_num <= 100 or user_num == STOP):
    user_num = int(input("Invalid input. Enter a number (1-100, 999 to quit): "))


# while the number is not equal to the sentinel value (999), continue the loop
while user_num != STOP:

    # increment count and add the number to the total
    COUNT += 1
    TOTAL += user_num

    # determine if the number is within the given range
    # hint: The last value can be the else clause since every other value after 68 would fall in this range
    # display the number and your results based on the met condition
    # hint: use f-strings to format your output
    if 91 < user_num <= 100:
        print(f"{user_num} is a A!")
    elif 83 < user_num <= 91:
        print(f"{user_num} is a B.")
    elif 75 < user_num <= 83:
        print(f"{user_num} is a C.")
    elif 67 < user_num <= 75:
        print(f"{user_num} is a D.")
    else:
        print(f"{user_num} is an F.")

    # prompt user for a new number
    user_num = int(input("Enter a number (1-100, 999 to quit): "))

    # validate the input for the number (1 - 100, or 999)
    while not (1 <= user_num <= 100 or user_num == STOP):
        user_num = int(input("Invalid input. Enter a number (1-100, 999 to quit): "))

# determine the average using the total and the count
average = TOTAL / COUNT
the_average = int(average)

if 91 < the_average <= 100:
    grade = "A"

elif 83 < the_average <= 91:
    grade = "B"

elif 75 < the_average <= 83:
    grade = "C"

elif 67 < the_average <= 75:
    grade = "D"

else:
    grade = "F"

# display the average grade.
print(f"The average grade was {the_average}. {the_average} is a {grade}.", end="")

# EXTRA CREDIT: +5 points for including in the program. +5 points for including in the flowchart.
# end the previous line of code with a space instead of a new line character
# hint: include end=" "

# determine if the average is within the given range.
# display the average and its results based on the met condition
