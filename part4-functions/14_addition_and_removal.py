# add and remove from a list
my_list = []
while True:
    print("The list is now",my_list)
    choice= input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        my_list.append(len(my_list)+1)
    elif choice == "r":
        my_list.pop(len(my_list)-1)
    else:
        print("Bye!")
        break
