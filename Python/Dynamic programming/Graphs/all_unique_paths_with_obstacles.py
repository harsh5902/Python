
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
def uniquePaths(m, n):
    if m>=0 and n>=0 and obstacleGrid[m][n]==1:
        return 0
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0

    up = uniquePaths(m-1, n)
    left = uniquePaths(m, n-1)
    return up+left

res = uniquePaths(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
print(res)

# Memoization
dp = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
def uniquePathsMemo(m,n):
    if m>=0 and n>=0 and obstacleGrid[m][n]==1:
        return 0
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    
    up = uniquePathsMemo(m-1, n)
    left = uniquePathsMemo(m, n-1)
    return up+left
    

res = uniquePathsMemo(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
print(res)


# Tabulation
def uniquePathsTab(m,n):
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i==0 and j==0:
                dp[i][j] = 1
            else:
                up = 0
                left = 0
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                dp[i][j] = up+left
    return dp[m-1][n-1]

dp = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
res = uniquePathsTab(len(obstacleGrid), len(obstacleGrid[0]))
print(res)
