# Write your solution here
def double_items(a):
    b=a[:]
    for i in range(len(b)):
        b[i] *= 2
    return b

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
