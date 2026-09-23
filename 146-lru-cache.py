class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        if len(self.cache) > self.cap:
            for lru in self.cache:
                break
            self.cache.pop(lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# submission 1873965351 - 2026-01-04T07:59:21+00:00
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        if len(self.cache) > self.cap:
            for lru in self.cache:
                break
            self.cache.pop(lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# submission 1873979015 - 2026-01-04T08:16:07+00:00
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next  = self.latest
        self.latest.prev = self.oldest
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# submission 2149171762 - 2026-09-22T00:20:51+00:00
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class LRUCache:
    # thoughts:
    # we have to use a doubly linked list here because insertion/deletion is O(1)
    # and we only really need to be looking at the heads, since we are evicting the least recently used, which will always be at the end 

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev 

    def insert(self, node):

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right

        self.right.prev = node    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # just accessed, so we remove and reinsert so that it is MRU
        self.remove(node)
        self.insert(node)

        return node.val

    

        

    

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # remove the value from recency list
            self.remove(self.cache[key]) 
        
        # create a node with the new key and value
        node = Node(key, value)
        # add to cache
        self.cache[key] = node
        # insert into the list
        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)