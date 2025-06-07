# Write your solution here
books_number={}
while True:
    
    setting=int(input("command (1 search, 2 add, 3 quit): "))

    if setting == 1:
        name=input("name: ")
        if name in books_number:
            for number in books_number[name]:
                print(number) 
        else:
            print("no number")
    elif setting == 2:
        name=input("name: ")
        number=input("number: ")
        if name in books_number:
            books_number[name].append(number)
        else:
            books_number[name]=[number]
        print("ok!")
    else:
        print("quitting...")
        break
