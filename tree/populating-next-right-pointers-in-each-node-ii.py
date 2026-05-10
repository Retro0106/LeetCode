"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if not root: return 
        # initialize deque as [root]
        # while queue:
            # for i in range(len(deque))
                # pop node from deque
                # if i == len(deque)-1:
                    # set node.next = null
                # else:
                    # set node.next = deque[i]
                # if node.left, add. same for right
        
        if not root: return
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == (length - 1):
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root