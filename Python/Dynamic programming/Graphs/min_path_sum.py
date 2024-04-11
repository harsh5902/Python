import sys
grid = [[1,3,1],[1,5,1],[4,2,1]]

#Recursion
def min_path_sum(m, n):
    if m==0 and n==0:
        return grid[m][n]
    if m<0 or n<0:
        return sys.maxsize

    up = grid[m][n] + min_path_sum(m-1, n)
    left = grid[m][n] + min_path_sum(m, n-1)
    return min(up,left)

res = min_path_sum(len(grid)-1, len(grid[0])-1)
print(res)

#Memoization
def min_path_sum_memo(m, n):
    if m==0 and n==0:
        return grid[m][n]
    if m<0 or n<0:
        return sys.maxsize
    if dp[m][n] != -1:
        return dp[m][n]

    up = grid[m][n] + min_path_sum(m-1, n)
    left = grid[m][n] + min_path_sum(m, n-1)
    return min(up,left)

dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
res = min_path_sum_memo(len(grid)-1, len(grid[0])-1)
print(res)


#Tabulation
def min_path_sum_tab(m, n):
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j] = grid[i][j]
            else:
                up = grid[i][j]
                if i>0:
                    up += dp[i-1][j]
                else:
                    up += sys.maxsize 
                
                left = grid[i][j]
                if j>0:
                    left += dp[i][j-1]
                else:
                    left+= sys.maxsize
                
                dp[i][j] = min(up, left)
    return dp[m-1][n-1]

dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
res = min_path_sum_tab(len(grid), len(grid[0]))
print(res)

