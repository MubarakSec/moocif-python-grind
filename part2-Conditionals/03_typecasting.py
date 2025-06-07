# Task: Ask for a positive float and print 
# the integer and decimal parts separately

num=float(input("type a number: "))
numint=int(num)
num=num-numint
print("Integer part:", numint)
print("Decimal part:", num)
