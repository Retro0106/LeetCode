class Node():
    def __init__(self, key,val):
        self.key,self.val = key, val
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.right = self.tail
        self.tail.left = self.head
        
    
    def remove(self, node):
        prev = node.left 
        next = node.right
        prev.right = next
        next.left = prev


    def insert(self, node):
        next = self.tail
        prev = self.tail.left
        node.right = next
        node.left = prev
        prev.right = node
        self.tail.left = node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) == self.capacity:
            self.cache.pop(self.head.right.key)
            self.remove(self.head.right)
        
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
            
        
        
        

        
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)