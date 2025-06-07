# Compare strings
sting= input("string1")
sting2 = input("string2")

if len(sting) > len(sting2):
    print(sting, "is longer")
elif len(sting) == len(sting2):
    print("The strings are equally long")
else:
    print(sting2, "is longer")
