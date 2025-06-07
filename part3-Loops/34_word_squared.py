# a square out of aybabtu word
def squared(s, n):
    length = len(s)
    for i in range(n):
        start = (i * n) % length
        row = ''.join([s[(start + j) % length] for j in range(n)])
        print(row)
if __name__ == "__main__":
    word=input("the word: ")
    times=int(input("enter a number of the border: "))
    squared(word,times)
