#https://www.youtube.com/watch?v=Rezetez59Nk&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=16

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def insert(root,data):
    if root == None:
        return Node(data)
    else:
        if data <= root.val:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data) 
    return root


root = None
root = insert(root, 1)
root = insert(root, 2)
# root = insert(root, 2)
# root = insert(root, 6)
# root = insert(root, 20)
# root = insert(root, 25)
# root = insert(root, 30)

def height(root, diameter):
    if not root:
        return 0

    lh = height(root.left, diameter)
    rh = height(root.right, diameter)

    diameter = max(diameter, lh+rh)
    return 1+max(lh, rh)

diameter = 0
height(root, diameter)
print(diameter)
