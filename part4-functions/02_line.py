# Write your solution here
# You can test your function by calling it within the following block
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

if __name__ == "__main__":
    line(5, "x")
