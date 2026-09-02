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