# Write your solution here
def print_sudoku(a):
    for i in range(len(a)):
        line=""
        for j in range(len(a[i])):
            num = a[i][j]
            val = "_" if num == 0 else str(num)
            line += val + " "
            if (j + 1) % 3 == 0 and j != 8:
                line += " "
        print(line.strip())
        if (i + 1) % 3 == 0 and i != 8:
            print()

def add_number(b:list, row:int, column:int, new_value:int):
    row=b[row]
    row[column]=new_value


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
