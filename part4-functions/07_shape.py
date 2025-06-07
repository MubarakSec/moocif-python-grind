# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def shape(size1,char1,size2,char2):
    # You should call function line here with proper parameters
    i = 1
    j = size2
    while i <= size1:
        line(i, char1)
        i += 1
    while 0 < j:
        line(size1,char2)
        j -=1
if __name__ == "__main__":
    shape(5, "x", 2, "o")
