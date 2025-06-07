# Repeatedly prints "hi" and asks "Shall we continue?" 
# until user types "no".
while True:
    print("hi")
    answer=input("Shall we continue?")
    if answer == "no":
        print("okay then")
        break
    