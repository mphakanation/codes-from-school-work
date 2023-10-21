# Get the number of packages purchased from the user
num_packages = int(input("Enter the number of packages purchased: "))

# Calculate the discount and total purchase amount
discount = 0
if num_packages >= 10 and num_packages <= 19:
    discount = 0.1
elif num_packages >= 20 and num_packages <= 49:
    discount = 0.2
elif num_packages >= 50 and num_packages <= 99:
    discount = 0.3
elif num_packages >= 100:
    discount = 0.4

total_amount = num_packages * 99 * (1 - discount)

# Display the results
if discount > 0:
    print("Congratulations! You received a discount of {:.0%}.".format(discount))
print("The total purchase amount is ${:.2f}.".format(total_amount))
