
#Optimization 1
nse = []
stack = [] 
heights = [2,1,5,6,2,3]
#Find next small on left
for i in range(len(heights)):
    while stack!=[] and heights[i]<=heights[stack[-1]]:
        stack.pop()
    if stack == []:
        nse.append(0)
    else:
        nse.append(stack[-1]+1)
    stack.append(i)
print("Previous smaller to left", nse)
    
#Find prev small on right
pse = []
stack = []
for i in range(len(heights)-1, -1, -1):
    while stack!=[] and heights[i]<=heights[stack[-1]]:
        stack.pop()
    if stack == []:
        pse.insert(0, len(heights)-1)
    else:
        pse.insert(0, stack[-1]-1)
    stack.append(i)

print("Previous smaller from right", pse)

max_area = 0
#Use that to calculate area

for i in range(len(heights)):
    area = (abs(pse[i]-nse[i])+1)*heights[i]
    max_area = max(area, max_area)

print(max_area)

