def isSafe(board, row, col, number):
    for i in range(9):
        if board[row][i] == str(number):
            return False
        
        if board[i][col] == str(number):
            return False
        
        sr = (3*int(row/3))
        sc = (3*int(col/3))

        for i in range(sr, sr+3):
            for j in range(sc, sc+3):
                if board[i][j] == str(number):
                    return False
    
    return True


def helper(board, row, col):
    if row == len(board):
        return True

    nrow = 0
    ncol = 0

    if col == len(board)-1:
        nrow = row + 1
        ncol = 0
    else:
        nrow = row
        ncol = col + 1
    
    if board[row][col] != '.':
        if helper(board, nrow, ncol):
            return True
    
    else:
        for i in range(1,10):
            if isSafe(board, row, col, i):
                board[row][col] = str(i)
                if helper(board, nrow, ncol):
                    return True
                else:
                    board[row][col] = '.'

    return False

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

helper(board, 0, 0)
print(board)

