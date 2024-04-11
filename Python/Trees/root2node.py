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

root = Node(6)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 8)
root = insert(root, 7)
root = insert(root, 9)
root = insert(root, 1)

def get_path(root, res, target):
    if not root:
        return False

    if root.val == target:
        return True

    res.append(root.val)
    get_path(root.left, res, target)
    get_path(root.right, res, target)


res = []
get_path(root, res, 9)
print(res)


