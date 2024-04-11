# There is a robot on an m x n grid. 
# The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Recursive Approach
def uniquePathsRecursive(m, n):
    if m==1 and n==1:
        return 1
    if m<1 or n<1:
        return 0
    
    up = uniquePathsRecursive(m-1, n)
    left = uniquePathsRecursive(m, n-1)
    return up+left

res = uniquePathsRecursive(3, 7)
print(res)


# DP approach (Memoization)
m = 3
n = 7
dp = [[-1]*n for _ in range(m)]
def uniquePathsMemo(m,n):
    if m==1 and n==1:
        return 1
    if m<1 or n<1:
        return 0
    if dp[m-1][n-1] != -1:
        return dp[m-1][n-1]
    
    up = uniquePathsMemo(m-1, n)
    left = uniquePathsMemo(m, n-1)

    return up+left

res = uniquePathsMemo(3, 7)
print(res)


# DP approach (Tabulation)
def uniquePathsTab(m, n):
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j] = 1
            else:
                up = 0
                left = 0
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                dp[i][j] = up + left
    return dp[m-1][n-1]


dp = [[-1]*n for _ in range(m)]
res = uniquePathsTab(3, 7)
print(res)


##If there is prev row or prev col we can space optimize it
# Space Optimization

def uniquePathsSO():
    pass

res = uniquePathsSO(3, 7)
print(res)

