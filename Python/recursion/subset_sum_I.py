arr = [3,1,4]
res = []
def subset_sum(array, idx, sum):
    if idx == len(array):
        res.append(sum)
        return

    subset_sum(arr, idx+1, sum+array[idx])
    subset_sum(arr, idx+1, sum)

subset_sum(arr, 0, 0)
res.sort()
print(res)