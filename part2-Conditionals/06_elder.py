# Ask for the name and age of the first person  
# Ask for the name and age of the second person  
# Compare the ages  
# Print the name of the older person  

name1=input("what thier name?")
age1=int(input("age?"))
name2=input("what thier name?")
age2=int(input("age?"))

if age1 > age2:
    print("The elder is", name1)
elif age2 > age1:
    print("The elder is", name2)
else:
    print(f"{name1} and {name2} are the same age")
