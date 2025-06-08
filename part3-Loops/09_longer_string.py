# Compare strings
string= input("string1: ")
string2 = input("string2: ")

if len(string) > len(string2):
    print(string, "is longer")
elif len(string) == len(string2):
    print("The strings are equally long")
else:
    print(string2, "is longer")
