# Data types, Numbers, operations, type conversion, f-strings

print("Hello"[0])

# umderscore can be use in place of comma for big numbers. E.g
123_123_409 

# Float - Data type with decimal, e.g
123.145

# Boolean
True
False

# concatenation
num_char = len(input("What is your Name?"))
# You can not concatenate integers and strings like below:
# print(num_char + "Great")

# instead, you should convert(type conversion or type casting)

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

# Addition(+), subtraction(-), multiplication(*), division(/), exponential(**)
# PEMDAS
# Parentithesis
# exponential
# multiplication
# Division
# Addition
# subtraction

print(int(1.62))
# rounding a floating number

print(round(8/3, 2))

score = 0
score += 1
print(score)
# f-string
print(f"your score is {score}")