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

inorder_trav = []
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    inorder_trav.append(root.val)
    inorder(root.right)

preorder_trav = []
def preorder(root):
    if root==None:
        return None
    preorder_trav.append(root.val)
    preorder(root.left)
    preorder(root.right)

postorder_trav = []
def postorder(root):
    if root == None:
        return None
    postorder(root.left)
    postorder(root.right)
    postorder_trav.append(root.val)


root = None
root = insert(root, 7)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 1)
print(root)

inorder(root)
print("Inorder Traversal: ", inorder_trav)

preorder(root)
print("Preorder Traversal: ", preorder_trav)

postorder(root)
print("Preorder Traversal: ", postorder_trav)