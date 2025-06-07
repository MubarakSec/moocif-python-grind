# has a vowel or not
string=input("type a word: ")
vowel= "aeoui"
index=0
while index < len(vowel):
    vowels = vowel[index]
    if vowels in string:
        print(vowels, "found")
    else:
        print(vowels, "not found")
    index +=1
