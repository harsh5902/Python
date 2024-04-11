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
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 20)
root = insert(root, 25)
root = insert(root, 30)

def helper(root):
    if not root:
        return 0 

    lh = helper(root.left)
    if lh == -1:
        return -1
    rh = helper(root.right)
    if rh == -1:
        return -1

    if abs(lh - rh)>1:
        return -1

    return 1+max(lh, rh)

def is_balanced(root):
    return helper(root) != -1


res = is_balanced(root)
print(res)