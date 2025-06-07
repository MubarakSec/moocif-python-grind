# Write your solution here
def count_matching_elements(a:list,numebr:int):
    counter=0
    for i in a:
        for j in i:
            if j==numebr:
                counter+=1
    return counter
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
