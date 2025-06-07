# Write your solution here
def times_ten(start,end):
    hmmm={}
    for i in range(start,end+1):
        hmmm[i] = i * 10
    return (hmmm)
if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
