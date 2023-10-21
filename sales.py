purchase_amount = float(input("Enter the amount of purchase: "))
state_tax = purchase_amount * 0.05
county_tax = purchase_amount * 0.025
total_tax = state_tax + county_tax
total_sale = purchase_amount + total_tax
print("Amount of purchase: $", purchase_amount)
print("State sales tax: $", state_tax)
print("County sales tax: $", county_tax)
print("Total sales tax: $", total_tax)
print("Total sale: $", total_sale)
