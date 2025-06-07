# find all the substrings
boss=input("what the main word")
servent=input("the branch caracter")
mathy=0

while len(boss)-3 >= mathy:
    if boss[mathy] == servent:
        print(boss[mathy:mathy+3])

    mathy+=1
