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

def copy_and_add(b:list, row:int, column:int, new_value:int):
    c=[i[:] for i in b]
    c[row][column]=new_value
    return c


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
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
