grid = [[2,1,1],[1,1,0],[0,1,1]]


q = []
visited = [[-1]*len(grid[0]) for _ in range(len(grid))]
count = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[i][j] == 2:
            q.append([[i,j], 0])
            visited[i][j] = 2
        else:
            visited[i][j] = 0
        
        if grid[i][j] == 1:
            count += 1

tm = 0
directions = [[0,1], [1,0], [-1,0], [0,-1]]
cnt = 0 
while q:
    vertex = q.pop(0)
    r = vertex[0][0]
    c = vertex[0][1]
    t = vertex[1]
    tm = max(tm, t)

    for i in range(4):
        nrow = r + directions[i][0]
        ncol = c + directions[i][1]
        if (nrow in range(len(grid))) and (ncol in range(len(grid[0]))) and (grid[nrow][ncol] == 1) and (visited[nrow][ncol] == 0):
            q.append([[nrow, ncol], t+1])
            visited[nrow][ncol] = 2
            cnt += 1

if count!= cnt:
    print(-1)
else:
    print(tm)
