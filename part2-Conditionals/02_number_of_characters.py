# Task: Ask the user for a word, 
# and if it contains more than one character,
# print the number of characters
word=input("Please type in a word:")
if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")
print("Thank you!")
