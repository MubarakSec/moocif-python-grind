# Multiple of 2 till the upper limit
upperlimit= int(input("enter the upper limit"))
exponant=0
number = 0
while number < upperlimit:
    number = 2 ** exponant
    if number<= upperlimit:
        print(number)
    exponant += 1
    