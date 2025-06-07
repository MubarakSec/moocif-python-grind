# start with low high low high
n= int(input("enter a number: "))
low=1
high=n
while low <= high:
    print(low)
    if low != high:
        print(high)
    high -= 1
    low +=1
