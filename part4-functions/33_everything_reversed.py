# Write your solution here
def everything_reversed(a):
    hello=[]
    for item in a:
        hello.append(item[::-1])
    return hello[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
