# Write your solution here
def create_tuple(x,y,z):

    return (min(x,y,z),max(x,y,z),x+y+z)
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
