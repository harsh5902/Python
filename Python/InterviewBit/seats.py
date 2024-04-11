#There are len(input) seats present
# . are the empty seats and x is person seated on specific seat
# Calculate the minimum number of jumps taken by people so that they will sit in a group
input = ['x','.','.','x','x', '.', '.', '.', 'x', '.']

def solution(arr):
    # Taking indexes of acquired seats
    x_index = []
    for i in range(len(arr)):
        if arr[i] == 'x':
            x_index.append(i)
    
    # Find median among x_index
    median = len(x_index)//2
    jumps = 0
    print(x_index)
    print(median)
    for i in range(len(x_index)): 
        start = x_index[i]
        end = x_index[median] - median + i
        jumps += (abs(end - start))
    
    return jumps

res = solution(input)
print(res)