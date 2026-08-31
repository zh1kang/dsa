class ListNode: 
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.freq = 1
        self.prev = None
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head 

    def length(self):
        return self.size

    def appendTail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
       
    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev 
        node.prev = None
        node.next = None
        self.size -= 1
    
    def popHead(self):
        if self.length == 0:
            return None
        node = self.head.next 
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0 
        self.node_map = {} # map key -> node
        self.list_map = defaultdict(LinkedList) # freq -> linked list of nodes 

    def counter(self, node):
        count = node.freq
        self.list_map[count].pop(node)

        if count == self.lfu_count and self.list_map[count].length() == 0:
            self.lfu_count += 1

        node.freq += 1
        self.list_map[node.freq].appendTail(node)


    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.counter(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.counter(node)
            return

        if len(self.node_map) == self.capacity:
            node = self.list_map[self.lfu_count].popHead()
            self.node_map.pop(node.key)
        
        node = ListNode(key, value)
        self.node_map[key] = node
        self.list_map[1].appendTail(node)
        self.lfu_count = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)