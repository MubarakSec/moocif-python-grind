# chessboard out of ones and zeros
def chessboard(chess):
    rows=0
    while rows < chess:
        col= 0
        line = ""
        while col < chess:
            if (col + rows) % 2 == 0:
                line += "1"
            else:
                line +="0"
            col += 1
        print(line)
        rows += 1

if __name__ == "__main__":
    chessboard(3)
