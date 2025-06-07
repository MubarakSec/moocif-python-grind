# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word: str):
    return word == word[::-1]

while True:
    idk=input("Please type in a palindrome: ")
    if palindromes(idk):
        print(idk, "is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
