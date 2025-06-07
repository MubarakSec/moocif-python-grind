# Ask for integers until 0 is typed and then print count, sum, and mean
#  of entered numbers (excluding zero).
# Also print how many of the numbers were positive
#  and how many were negative.

typednum= 0
sumnum=0
meannum=0
postnum=0
negativenum=0
print("Please type in integer numbers. Type in 0 to finish.")
num =1
while num != 0:
    num=int(input("Number: "))
    if num == 0:
        break
    typednum +=1
    sumnum += num
    if num > 0:
        postnum +=1
    else:
        negativenum += 1
print("Numbers typed in", typednum)
print("The sum of the numbers is", sumnum)
print("The mean of the numbers is", (sumnum / typednum))
print("Positive numbers", postnum)
print("Negative numbers", negativenum)
