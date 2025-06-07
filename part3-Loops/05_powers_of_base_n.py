# Multiable of the base until the upper limit
upperlimit= int(input("enter the upper limit"))
exponant=0
number2 = 0
base=int(input("base"))
while number2 <= upperlimit:
    number2 = base ** exponant
    if number2<= upperlimit:
        print(number2)
    exponant += 1
