# Write your solution here
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
