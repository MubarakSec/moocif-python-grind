# Write your solution here
while True:
    editor=input("what editor you use: ")
    if "visual studio code" == editor.lower():
        print("an excellent choice!")
        break
    elif editor.lower() == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
