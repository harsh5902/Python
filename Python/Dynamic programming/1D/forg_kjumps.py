import sys


def frog_k_jumps(idx, jumps, k):
    if idx == 0:
        return 0
    min_step = sys.maxsize
    for i in range(1, k+1):
        if idx-i >= 0:
            jump = frog_k_jumps(idx-i ,jumps, k) + abs(jumps[idx] - jumps[idx-i])
            min_step = min(jump, min_step)
    
    return min_step

#Memoization
def frog_k_jumps_memo(idx, jumps, k, dp):
    if idx == 0:
        return 0

    if dp[idx]!=-1:
        return dp[idx]

    min_step = sys.maxsize

    for i in (1, k+1):
        if idx-i>=0:
            jump = frog_k_jumps_memo(idx-i ,jumps, k, dp) + abs(jumps[idx] - jumps[idx-i])
            min_step = min(jump, min_step)
    dp[idx] = min_step
    return dp[idx]

jumps = [30, 10, 60, 30, 60, 50]
k = 3
res = frog_k_jumps(len(jumps)-1, jumps, k)
print(res)

dp = [-1]*(len(jumps))
res = frog_k_jumps_memo(len(jumps)-1, jumps, k, dp)
print(dp)
print(res)