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
root = insert(root, 8)
root = insert(root, 9)
root = insert(root, 3)
root = insert(root, 4)


def getVerticalOrder(root, hd, m):
    if not root:
        return
    try:
        m[hd].append(root.val)
    except:
        m[hd] = [root.val]
    getVerticalOrder(root.left, hd-1, m)
    getVerticalOrder(root.right, hd+1, m)



def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)
    print(m)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end=" ")
        print()

printVerticalOrder(root)