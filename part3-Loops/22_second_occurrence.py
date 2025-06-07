# print the second occurrence only

text = input("Please type in a string: ")
sub = input("Please type in a substring: ")

first_index = text.find(sub)

if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    second_index = text.find(sub, first_index + len(sub))
    
    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
