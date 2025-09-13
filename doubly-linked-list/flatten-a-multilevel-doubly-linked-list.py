"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        dummy.next = head
        stack = [head]
        curr = dummy

        while stack:
            temp = stack.pop()
            if temp.next: stack.append(temp.next)
            if temp.child: stack.append(temp.child)

            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = curr.next
        
        dummy.next.prev = None
        return dummy.next
        