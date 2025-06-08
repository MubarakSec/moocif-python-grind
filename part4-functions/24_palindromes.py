# is the word can be read from both side
def palindromes(word: str):
    return word == word[::-1] #to revers the word

while True:
    idk=input("Please type in a palindrome: ")
    if palindromes(idk):
        print(idk, "is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
