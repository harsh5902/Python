class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def insert(root, data):
    if root == None:
        return Node(data)
    else:
        if data <= root.val:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data) 
    return root


root = Node(6)
root = insert(root, 8)
root = insert(root, 4)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 7)
root = insert(root, 9)
root = insert(root, 1)

#Apply reverse preorder traversal
def rightView(root, res, level):
    if not root:
        return
    
    if level == len(res):
        res.append(root.val)
    rightView(root.right, res, level+1)
    rightView(root.left, res, level+1)

res = []
rightView(root, res, 0)
print(res)