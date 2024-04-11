grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

visited = set()

def bfs(r, c):
    visited.add((r,c))
    q = [(r,c)]

    while q:
        vr, vc = q.pop(0)
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
        for dr, dc in directions:
            if (vr+dr in range(len(grid))) and (vc+dc in range(len(grid[0]))) and (grid[vr+dr][vc+dc]=="1") and ((vr+dr, vc+dc) not in visited):
                visited.add((vr+dr, vc+dc))
                q.append((vr+dr, vc+dc))
    return


islands = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (grid[i][j]=="1") and ((i,j) not in visited):
            bfs(i,j)
            islands += 1

print("Number of islands: ", islands)





