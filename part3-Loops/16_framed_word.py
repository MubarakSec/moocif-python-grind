# A word in a box
name= input("enter a word: ")
astrix="*"*30
middle= 28

total_width= middle - len(name)
left_side= total_width // 2
right_side= total_width - left_side
print(astrix)
print("*"," "*left_side,name,right_side*" ","*",sep="")
print(astrix)
