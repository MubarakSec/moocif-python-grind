# Write your solution here
def row_correct(sudoku:list,row:int):
    seen = []
    for num in sudoku[row]:
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True

def column_correct(sudoku:list,column:int):
    seen = []
    for row in sudoku:
        num = row[column]
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True

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

def sudoku_grid_correct(sudoku_ch):
    for i in range(9):
        if not row_correct(sudoku_ch,i):
            return False
    for i in range(9):
        if not column_correct(sudoku_ch,i):
            return False
    for row in [0,3,6]:
        for column in [0,3,6]:
            if not block_correct(sudoku_ch, row , column):
                return False
    return True

