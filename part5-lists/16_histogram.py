# Write your solution here
def histogram(a):
    counter={}
    for i in a:
        if i not in counter:
            counter[i]=0
        counter[i]+=1
    for char,times in counter.items():
        print(char, times * "*")
        



if __name__ == "__main__":
    histogram("abba")
