# Ask for integers until 0 is typed, then print count, sum, mean,
# number of positives, and number of negatives.

count= 0
total=0
positive=0
negative=0
print("Please type in integer numbers. Type in 0 to finish.")
num =1
while num != 0:
    num=int(input("Number: "))
    if num == 0:
        break
    count +=1
    total += num
    if num > 0:
        positive +=1
    else:
        negative += 1
print("Numbers typed in", count)
print("The sum of the numbers is", total)
print("The mean of the numbers is", (total / count) if count > 0 else 0)
print("Positive numbers", positive)
print("Negative numbers", negative)
