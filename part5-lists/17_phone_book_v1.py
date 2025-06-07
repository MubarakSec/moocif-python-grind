# Write your solution here
books_number={}
while True:
    
    setting=int(input("command (1 search, 2 add, 3 quit): "))

    if setting == 1:
        name=input("name: ")
        if name in books_number:
            print(books_number[name])
        else:
            print("no number")
    elif setting == 2:
        name=input("name: ")
        number=input("number: ")
        books_number[name]=number
        print("ok!")
    else:
        print("quitting...")
        break
