class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUcache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        #left --> Least Recently Used(LRU) && right --> Most Recently Used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self,node):
        prv, nxt = self.right.prev, self.right
        prv.next, node.prev = node, prv
        node.next, nxt.prev = nxt, node

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.cap<len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
obj = LRUcache(2)
obj.put(1, 1); # cache is {1=1}
obj.put(2, 2); # cache is {1=1, 2=2}
obj.get(1);    # return 1
obj.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
obj.get(2);    # returns -1 (not found)
obj.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
obj.get(1);    # return -1 (not found)
obj.get(3);    # return 3
obj.get(4);    # return 4

print(obj.cache)