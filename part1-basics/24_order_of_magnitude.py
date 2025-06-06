# Task: Ask for an integer and print messages 
# about its size according to thresholds (<1000, <100, <10)

number = int(input("number?"))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")
