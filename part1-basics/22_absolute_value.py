# Task: Ask for an integer, print its absolute value 
# (convert negative to positive)
number = int(input("nubmer?"))
if number < 0:
    number *= -1

print(f"The absolute value of this number is {number}")
