# Teaching how to add to a list
my_list = []
items=int(input("how many inputs: "))

while len(my_list) < items:
    value = int(input("value: "))
    my_list.append(value) 

print(my_list)
