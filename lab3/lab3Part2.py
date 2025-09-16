# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 9/17/25
# PROGRAM: Programming Lab 3, Part 2
# PURPOSE: Calculate the sales tax for a purchase.
# =================================================================

# get the subtotal from the user
subtotal = float(input("Enter the subtotal: "))

# set the sales tax
tax_rate = subtotal * .07

# set the sales total
sales_total = subtotal + tax_rate

# display subtotal, sales tax, and total
print(
        f"Subtotal:  ${subtotal:,.2f}\n"
        f"Sales tax: ${tax_rate:,.2f}\n"
        f"Total:     ${sales_total:,.2f}"
)
