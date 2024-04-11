perm = [1,2,3]
res = []

def all_combinations(arr, idx, subarr):
    if len(subarr) == len(arr):
        res.append(subarr)
        return
    
    for i in range(len(perm)):
        if arr[i] not in subarr:
            all_combinations(arr, idx+i, subarr+[arr[i]])


def find_permutations(arr, idx, subarr):
    if len(subarr) == len(arr):
        res.append(subarr)
        return
    
    for i in range(len(perm)):
        if arr[i] not in subarr:
            find_permutations(arr, idx+i, subarr+[arr[i]])

find_permutations(perm, 0, [])
print("All Permutations: \n", res)
all_combinations(perm, 0, [])
print("\n\nAll Permutations with duplicate allowed: \n", res)