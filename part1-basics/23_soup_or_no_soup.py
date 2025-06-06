# Task: Ask for user name, if not "Jerry", ask portions 
# and print total cost (5.90 per portion), else print "Next please!"
name = input("Your Name?")

if name == "Jerry": 
    print("Next please!")
else:
    print("The total cost is",int(input("how many scopes do you want?")) * 5.90)
    print("Next please!")
