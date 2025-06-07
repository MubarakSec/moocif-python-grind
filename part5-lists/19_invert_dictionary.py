# Write your solution here
def invert(a):
    inverted={}
    
    for i,k in a.items():
        inverted[k]=i
        
    a.clear()
    a.update(inverted)
if __name__ == "__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)
