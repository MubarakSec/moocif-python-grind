# Minecraft house
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

if __name__ == "__main__":
    square_of_hashes(5)
