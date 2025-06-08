# The Shortest string in the list
def shortest(my_list):
    return min(my_list, key=len) if my_list else ""
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
