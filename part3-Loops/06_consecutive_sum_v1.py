# Ask user for a limit, then sum consecutive numbers 
# until the sum meets or exceeds it.
number=int(input("LIMIT: "))
total = 0
number2=1
while total < number:
    total += number2
    number2 +=1
print(total)
