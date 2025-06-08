# start with one and end in 5 #
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(5)
