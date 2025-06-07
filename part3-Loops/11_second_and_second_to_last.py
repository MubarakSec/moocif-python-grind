# are they the same or not
word=input("word?")
if word[1] == word[-2]:
    print(f"The second and the second to last characters are {word[1]}")
else:
    print("The second and the second to last characters are different")
