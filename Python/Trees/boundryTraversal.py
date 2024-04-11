class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, data):
    if not root:
        return Node(data)
    
    if data <= root.val:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root

root = Node(6)
root = insert(root, 3)
root = insert(root, 8)
root = insert(root, 7)
root = insert(root, 9)
root = insert(root, 1)

def left_trav(root, res):
    if not root.left and not root.right:
        return res
    
    res.append(root.val)
    left_trav(root.left, res)

def leaf_nodes(root, res):
    if not root:
        return res

    if not root.left and not root.right:
        res.append(root.val)
    
    leaf_nodes(root.left, res)
    leaf_nodes(root.right, res)

def right_trav(root, res):
    if not root.left and not root.right:
        return res
    
    right_trav(root.right, res)
    res.append(root.val)

    return res

#Anti clockwise boundry traversal
def anticlk_boundry_traversal(root):
    res = []
    if not root: 
        return res
    left_trav(root, res)
    leaf_nodes(root, res)
    right_trav(root, res)
    return res

def clk_boundry_traversal(root):
    res = []
    if not root: 
        return res
    right_trav(root, res)
    leaf_nodes(root, res)
    left_trav(root, res)
    return res

output1 = anticlk_boundry_traversal(root)
print(output1[:-1])

