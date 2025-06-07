# Keep asking for words and print the story 
# when "end" is typed or the same word is typed twice
# in a row.

story = ""
word1= ""
attempts = 0
while True:
    word= input("Please type in a word:")
    attempts+= 1
    if word == "end" or word1 == word:
        break
    story += word + " "
    word1=word
print(story)
