from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # if not rott: return []
        # initialize deque, result
        # while queue:
            # initialize curr
            # for _ in range
                # pop node, add value to curr, if children, extend it to queue
            # add curr to result
        # return result

        if not root: return []
        queue = deque([root])
        result = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(curr)
        return result