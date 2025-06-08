# It prints as you want
def line(number, char):
    if char == "":
        char = "*"
    print(number * char[0])

def shape(size1,char1,size2,char2):
    i = 1
    j = size2
    while i <= size1:
        line(i, char1)
        i += 1
    while 0 < j:
        line(size1,char2)
        j -=1
if __name__ == "__main__":
    numbers=int(input("Enter a number: "))
    building_block=input("with what to build it: ")
    numbers_base=int(input("Number of fundumantions: "))
    base_block=input("base block: ")
    shape(numbers, building_block, numbers_base, base_block)
