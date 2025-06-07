# print the multiplication table till the base 
base = int(input("a number to start with: "))
start = 1
while start <= base:
    multiplywith=1
    while base >= multiplywith:
        print(f"{start} x {multiplywith} = {start*multiplywith}")
        multiplywith +=1
    start +=1 
