arr = [10,1,2,7,6,1,5]
target = 8
res = []

def combination_sum(arr, idx, target, subarr):
    if target==0:
        res.append(list(subarr))
        return

    for i in range(idx, len(arr)):
        if i>idx and arr[i]==arr[i-1]:
            continue
        elif target<arr[i]:
            break

        subarr.append(arr[i])
        combination_sum(arr, i+1, target-arr[i], subarr)
        subarr.pop()

arr.sort()
combination_sum(arr, 0, target, [])
print(res)