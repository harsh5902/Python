hashmap = {}
nums = [1,0,0,2,1,3,1,1,1]
k = 3
sum_ = 0
max_len = 0
for i in range(len(nums)):
    sum_ += nums[i]
    hashmap[sum_] = i
    if sum_ == k:
        max_len = max(max_len, i+1)

    rem = sum_ - k
    if rem in hashmap.keys():
        length = i - hashmap[rem]
        max_len = max(max_len, length)
    
    if sum_ not in hashmap:
        hashmap[sum_] = i

print(max_len)


# Optimal solution (Two pointer approach)

