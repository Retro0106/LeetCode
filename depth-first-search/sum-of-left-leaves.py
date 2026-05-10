from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # if not root: return 
        # initialize deque as [(False,root)]
        # total = 0
        # while queue:
            # for _ in range(len(queue)):
                # pop boolean, node
                # if node is leaf and bollean is true, add node.val to total
                # if node.left: add (True, node.left)
                # if node.right: add (False, node.right)
        # return total

        if not root: return 0
        queue = deque([(False, root)])
        total = 0
        while queue:
            for _ in range(len(queue)):
                left, node = queue.popleft()
                if not node.left and not node.right and left:
                    total += node.val
                if node.left: queue.append((True, node.left))
                if node.right: queue.append((False, node.right))
        return total
