class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.head, self.tail = None, None

class Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    # helper functions
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def insert(self, node):
        prevNode, nextNode = self.head, self.head.next
        prevNode.next, nextNode.prev = node, node
        node.prev = prevNode
        node.next = nextNode

    # getter function
    def get(self, key: int):
        if key in self.cache:
            # we need to remove from DLL
            self.remove(self.cache[key])

            # we need to insert it into the front of the DLL
            self.insert(self.cache[key])

            # return value
            return self.cache[key].val

        # if key not in cache, return -1
        return -1

    # setter function
    def put(self, key: int, val: int):
        # check if key is already in cache
        if key in self.cache:
            # remove it from DLL
            self.remove(self.cache[key])
        
        # create a new node containing key and val and put it in the cache
        self.cache[key] = Node(key, val)

        # insert this new node in the DLL
        self.insert(self.cache[key])

        # check if length of cache > capacity
        if len(self.cache) > self.capacity:
            # remove lru from DLL
            lru = self.tail.prev
            self.remove(lru)

            # delete the pointer to lru from cache
            del self.cache[lru.key]
        
    