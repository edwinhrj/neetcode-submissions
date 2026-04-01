class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None # LR pointers

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1) # create left right nodes
        self.left.next, self.right.prev = self.right, self.left

    # insert at right of LL
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    # remove from LL
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove then insert at right of LL since its MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key in self.cache: # if key alr exists
            # remove from LL
            self.remove(self.cache[key])
            # delete from cache
            del self.cache[key]

            # insert new Node

            self.insert(node)
            self.cache[key] = node
        
        else:
            # if hit/exceed capacity
            if self.capacity <= len(self.cache):
                # remove LRU
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

                # insert new node
                self.insert(node)
                self.cache[key] = node
            else:
                # insert new node
                self.insert(node)
                self.cache[key] = node
        

        
