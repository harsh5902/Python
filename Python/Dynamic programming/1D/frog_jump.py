import sys

# Recursive Solution
def frog_jump(idx, heights):
    if idx == 0:
        return 0 
    
    left = frog_jump(idx-1,heights) + abs(heights[idx] - heights[idx-1])
    if idx > 1:
        right = frog_jump(idx-2,heights) + abs(heights[idx] - heights[idx-2])
    else:
        right = sys.maxsize
    
    return min(left, right)
        
# DP solution
def frog_jump_dp(idx, heights, dp):
    if idx == 0:
        return 0
    
    if dp[idx] != -1:
        return dp[idx]
    
    left = frog_jump_dp(idx-1,heights, dp) + abs(heights[idx-1] - heights[idx])
    if idx > 1:
        right = frog_jump_dp(idx-2,heights, dp) + abs(heights[idx-2] - heights[idx])
    else:
        right = sys.maxsize
    dp[idx] = min(left, right)
    return dp[idx]

#Tabulation
def frog_jump_tab(jumps):
    dp = [-1]*len(jumps)
    dp[0] = 0
    for i in range(1, len(jumps)):
        jump1 = dp[i-1] + abs(jumps[i-1] - jumps[i])
        jump2 = sys.maxsize

        if i > 1:
            jump2 = dp[i-2] + abs(jumps[i-2] - jumps[i])

        dp[i] = min(jump1, jump2)

    return dp[-1]

#Space Optimization
def frog_jump_so(jumps):
    prev = 0
    prev2 = 0
    for i in range(1, len(jumps)):
        jump1 = prev + abs(jumps[i-1] - jumps[i])
        jump2 = sys.maxsize

        if i > 1:
            jump2 = prev2 + abs(jumps[i-2] - jumps[i])

        cur = min(jump1, jump2)
        prev2 = prev
        prev = cur
    return prev


jumps = [30, 10, 60, 10, 60, 50]
# dp = [-1]*len(jumps)
# res = frog_jump_dp(len(jumps)-1, jumps, dp)
# print(res)

res = frog_jump_so(jumps)
print(res)