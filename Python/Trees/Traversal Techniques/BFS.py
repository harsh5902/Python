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


def bfs(root):
    bfs_trav = []
    queue = []
    queue.append(root)

    while len(queue)>0:
        cur = queue.pop(0)
        bfs_trav.append(cur.val)

        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    
    return bfs_trav

root = None
root = insert(root, 7)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 1)
root = insert(root, 8)
root = insert(root, 11)

print(root)

res = bfs(root)
print("Breadth First Search Traversal: ", res)

