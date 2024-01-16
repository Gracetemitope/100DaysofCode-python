# Conditional statements, logical operators, code blocks and scope

print("Welcome to the Rollercoaster")
height = input("What is your height in cm ")

if int(height) >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How are old are you?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want to a photo? Y or N ")
    if photo == "Y":
        bill += 3
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")

else:
    print("Sorry! You have to grow a little taller to ride the roller coaster.")