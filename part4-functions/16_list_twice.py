# Print two list ordered and the original
my_list=[]
while True:
    word=new_value=int(input("new value or 0 to exit "))
    
    if new_value == 0:
        print("Bye!")
        break
    my_list.append(word)
    print("The list now:",my_list)
    print("The list in order:",sorted(my_list))
