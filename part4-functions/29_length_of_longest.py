# Write your solution here
def length_of_longest(my_list):
    return len(max(my_list, key=len )) if my_list else ""
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
