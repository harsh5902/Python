def dfs(board, r, c, visited):
    visited.add((r, c))
    directions = [[0,1], [1,0], [-1,0], [0,-1]]

    for direction in directions:
        nr, nc = (r+direction[0]), (c+direction[1])
        if (nr in range(len(board))) and (nc in range(len(board[0]))) and ((nr, nc) not in visited) and (board[nr][nc]=="O"):
            visited.add((nr, nc))
            dfs(board, nr, nc, visited)

board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]


visited = set()
for i in range (len(board)):
    for j in range(len(board[0])):
        if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and (board[i][j] == "O") and ((i, j) not in visited):
            dfs(board, i, j, visited)

print(visited)
for i in range(len(board)):
    for j in range(len(board[0])):
        if (board[i][j] == "O") and ((i, j) not in visited):
            board[i][j] = "X"

print(board)