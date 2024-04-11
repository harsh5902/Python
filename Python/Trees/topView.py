class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, data):
    if not root:
        return Node(data)
    
    if data<=root.val:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

root = Node(6)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 8)
root = insert(root, 7)
root = insert(root, 9)

def get_topview(root, hd, tree_dict):
    if not root:
        return

    if hd not in tree_dict.keys():
        tree_dict[hd] = root.val

    get_topview(root.left, hd-1, tree_dict)
    get_topview(root.right, hd+1, tree_dict)
    

def print_topview(root):
    tree_dict = {}
    hd = 0
    get_topview(root, hd, tree_dict)
    print(sorted(tree_dict))

    for idx, value in enumerate(sorted(tree_dict)):
        print(tree_dict[value])

print_topview(root)