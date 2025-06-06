# Task: Fix loyalty points bonus program to correctly 
# apply either 10% or 15% bonus but not both
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

else:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")
