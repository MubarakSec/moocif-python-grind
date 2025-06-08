# Minecraft house in better way
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1


if __name__ == "__main__":
    box_of_hashes(5)
