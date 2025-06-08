# Just a spruce

def spruce(hight):
    print("a spruce!")
    row = 0
    while row < hight:
        
        star= "*" *(row * 2 + 1)
        space= " " *(hight - row - 1)
        print(space + star)
        row +=1
        
    print (" "*(hight - 1) + "*")

if __name__ == "__main__":
    spruce(5)
