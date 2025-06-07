# Write your solution here
def block_correct(sudoku, row_no, column_no):
    seen = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            num = sudoku[i][j]
            if num != 0:
                if num in seen:
                    return False
                seen.append(num)
    return True

