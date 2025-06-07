# Multiple of 2 till the upper limit
upperlimit= int(input("enter the upper limit"))
exponant=0
number2 = 0
while number2 < upperlimit:
    number2 = 2 ** exponant
    if number2<= upperlimit:
        print(number2)
    exponant += 1
    