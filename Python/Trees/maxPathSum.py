class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, data):
    if root == None:
        return Node(data)

    if data <= root.val:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

root = Node(9)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 15)
root = insert(root, 7)

max_sum = []
def maxPath(root, maxi):
    if not root:
        return 0
    
    lh = max(0, maxPath(root.left, maxi))
    rh = max(0, maxPath(root.right, maxi))

    maxi = max(maxi, lh+rh+root.val)
    if max_sum == []:
        max_sum.append(maxi)
    else:
        max_sum[0] = maxi
    return root.val+max(lh, rh)

maxi = 0
maxPath(root, maxi)
print(max_sum[0])