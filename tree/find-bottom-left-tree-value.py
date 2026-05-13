from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # if not root: return None
        # initialize queue as deque
        # while queue:
            # left = queue[0]
            # for _ in range(deque), pop node, add left, add right
        # return left

        if not root: return None
        queue = deque([root])
        while queue:
            left = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return left

