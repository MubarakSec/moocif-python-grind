# Write your solution here
def list_sum(a,b):
    return [y+x for y,x in zip(a,b)]
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a,b)) # [8, 10, 12]
