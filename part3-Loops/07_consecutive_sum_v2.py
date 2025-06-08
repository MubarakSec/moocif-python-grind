# Gives more info how it is done
limit = int(input("LIMIT: "))
total = 0
current = 1
parts = []

while total < limit:
    total += current
    parts.append(str(current))
    current += 1

expression = " + ".join(parts) + f" = {total}"
print("The consecutive sum:", expression)
