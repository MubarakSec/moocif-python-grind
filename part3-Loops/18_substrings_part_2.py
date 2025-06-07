# it prints all the char till the full word 
# Starting from the last char
text=input("inter a string:")
index=1
while index <= len(text):
    print(text[-index:])
    index +=1
