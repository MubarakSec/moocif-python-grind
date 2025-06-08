# Multiable of the base until the upper limit
upperlimit= int(input("enter the upper limit: "))
exponant=0
number = 0
base=int(input("base: "))
while number <= upperlimit:
    number = base ** exponant
    if number<= upperlimit:
        print(number)
    exponant += 1
