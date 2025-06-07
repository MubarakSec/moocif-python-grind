# the factorial number

while True:
    number= int(input("Please type in a number: "))
    i =1
    total=1
    if number > 0:
        while number >= i:
            total *= i
            i += 1 
        print(f"The factorial of the number {number} is {total}")
    else:
        print("Thanks and bye!")
        break
