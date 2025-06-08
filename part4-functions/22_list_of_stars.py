# for each number in the list represented by a star
def list_of_stars(num :list):
    for i in num:
        print("*"*i)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
    
