# the range between the number. Zero excluded
Num = int(input("enter a number: "))
for i in range(-Num,Num+1):
    if i == 0:
        continue
    print(i)
