class LinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def pop_lru(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        node.next = None
        node.prev = None
        return node

class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.ll = LinkedList()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.ll.remove(node)
            self.ll.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.ll.remove(node)
            self.ll.insert(node)
            node.val = value
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                node_to_be_removed = self.ll.pop_lru()
                del self.cache[node_to_be_removed.key]
                
            self.cache[key] = node
            self.ll.insert(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)