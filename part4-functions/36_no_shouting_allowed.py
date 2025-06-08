# No Uppercharaters words
def no_shouting(a):
    no_upper=[]
    for up in a:
        if not up.isupper():
            no_upper.append(up)
    return no_upper

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
