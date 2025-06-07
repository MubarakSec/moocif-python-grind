# Gives more info how it is done
number=int(input("LIMIT:"))
total = 0
sum=1
final = f"The consecutive sum:"
while total < number:
    total += sum
    final += f" {sum} "
    if total < number:
        final += f"+ "
    else:
        final += f"= {total}"
    sum +=1

print(final)
