print("Welcome to the tip Calculator")

total_bill = input("What was the total bill?\n")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
no_of_splitters = input("How many people to split the bill?\n")
# calculate the tip
actual_tip = int(percentage_tip) / 100 * int(total_bill)
# Adding tip and total bill
new_total = int(total_bill) + int(actual_tip)
# Each contribution
each_contribution = int(new_total) / int(no_of_splitters)
rounded_value = round(each_contribution, 2)
print(f"Each person should pay {rounded_value}")

# Note: I was not able to round the value to 2 decimal place

