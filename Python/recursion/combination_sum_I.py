arr = [2,3,6,7]
target = 7
res = []
def combination_sum(arr, idx, target, subarr):
    if idx==len(arr):
        if target == 0:
            res.append(subarr.copy())
        return

    if arr[idx] <= target:
        subarr.append(arr[idx])
        combination_sum(arr, idx, target-arr[idx], subarr)
        subarr.remove(subarr[len(subarr)-1])

    combination_sum(arr, idx+1, target, subarr)

combination_sum(arr, 0, target, [])
print(res)