# Write your solution here
def factorials(n):
    fact={}
    total=1
    for i in range(1 , n+1):
        total*=i
        fact[i]=total
    return fact

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
