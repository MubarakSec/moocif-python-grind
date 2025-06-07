# Ask for two lowercase words  
# Print the one that comes last alphabetically  

name1=input("what thier name?")
name2=input("what thier name?")

if name1 > name2:
    print(name1," comes alphabetically last.")
elif name2 > name1:
    print(name2," comes alphabetically last.")
else:
    print(f"You gave the same word twice.")
