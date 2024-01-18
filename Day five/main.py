# Python Loops
Names = ["Temi", "Blessing", "Samuel", "Mena"]
for Name in Names:
    print(Name)
    print(Name + " human")
    print(Names)

for number in range(1, 10):
    print(number)


# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇
# total_even_number = 0
# for number in range(0, target+1):
#   if number % 2 == 0:
#     total_even_number += number
# print(total_even_number)


# FizzBuzz game: Write your code here 👇
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
      print("Buzz")
  # elif number % 3 == 0 and number % 5 == 0:
  #   print("FizzBuzz")
  else:
    print(number)