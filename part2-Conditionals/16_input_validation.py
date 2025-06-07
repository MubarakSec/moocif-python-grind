# Ask for integers until 0; print sqrt if positive, 
# else "Invalid number".

from math import sqrt
# Write your solution here
while True:
    number=int(input("enter an number"))
    if number == 0:
        print("Exiting...")
        break
    elif number > 0:
        print(sqrt(number))
    else:
        print("Invalid number")
