# How does a def function work
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

if __name__ == "__main__":
    line(5, "x")
