arr = [1,2,3,4,5,6,7,7,8]
subarrs = []
for i in range(len(arr)+1):
    for j in range(i+1, len(arr)+1):
        subarr = []
        for k in range(i, j):
            subarr.append(arr[k])
        subarrs.append(subarr)

print(subarrs)
    