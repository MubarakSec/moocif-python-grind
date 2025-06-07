# it find the first occurrence of the substring
boss=input("what the main word: ")
servent=input("the branch caracter: ")
mathy=boss.find(servent)
#the find() return -1 when it does not find anything
if mathy != -1 and mathy+3 <= len(boss):
    print(boss[mathy:mathy+3])
