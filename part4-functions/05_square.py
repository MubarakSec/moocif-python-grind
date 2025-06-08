# Change of the building block
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def square(size, character):
    
    i = 0
    while i < size:
        line(size, character)
        i += 1

if __name__ == "__main__":
    square(5, "x")
