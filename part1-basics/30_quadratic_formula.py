# Task: Solve quadratic equation ax²+bx+c 
# using quadratic formula, print both real roots;
# assume two real roots always


# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a=int(input("value of a:"))
b=int(input("value of b:"))
c=int(input("value of c:"))

postivex = (-b + sqrt((b*b)-(4*a*c)))/(2*a)
negtivex = (-b - sqrt((b*b)-(4*a*c)))/(2*a)

print(f"The roots are {postivex} and {negtivex}")
