# prints the first char in the word
sentence= input("Please type in a sentence: ")
sentence= " " + sentence
i=0
while i < len(sentence):
    if sentence[i] == " ":
        i+=1
        if i < len(sentence) and sentence[i] != " ":
            print(sentence[i])
        continue
    i += 1
