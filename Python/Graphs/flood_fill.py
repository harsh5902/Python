############### Given ################
image = [[1,1,1], [1,1,0], [1,0,1]]
sr, sc = 1, 1
color = 2
######################################


initial = image[sr][sc]
ans = image

def dfs(image, initial, r, c, color, directions):
    image[r][c] = color
    n = len(image)
    m = len(image[0])
    for i in range(0, 4):
        nrow = r + directions[i][0]
        mcol = c + directions[i][1]
        if (nrow in range(len(image))) and (mcol in range(len(image[0]))) and (image[nrow][mcol]==initial) and (image[nrow][mcol]!=color):
            dfs(image, initial, nrow, mcol, color, directions)
    
    
directions = [[1,0], [0,1], [-1,0], [0,-1]]
dfs(ans, initial, sr, sc, color, directions)
print(ans)

