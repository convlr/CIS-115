# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 9/25/25
# PROGRAM: Programming Lab 5, Part 2
# PURPOSE: The discount calculator determines if the user has
#          purchased enough items or spent enough money to qualify
#          for a 20% or 10% discount on their purchase.
# =================================================================

# get the subtotal and quantity from the user
subtotal = float(input("Enter the subtotal: "))
quantity = int(input("Enter the quantity: "))

# if-elif-else to determine discount
if quantity >= 50 or subtotal >= 10:
	discount = subtotal * .20
	print("You qualify for a 20% discount!")
elif quantity >= 15 or subtotal >= 50:
	discount = subtotal * .10
	print("You qualify for a 10% discount!")
else:
	print("You do not qualify for a discount.")

# set the sales tax
sales_tax = (subtotal - discount) * .07

# set the sales total
sales_total = subtotal + sales_tax - discount

# display subtotal, discount, sales tax, and total
print(f'''Subtotal:  {subtotal:.2f}
Discount:  {discount:.2f} 
Sales tax: {sales_tax:.2f}
Total:     {sales_total:.2f}''')
