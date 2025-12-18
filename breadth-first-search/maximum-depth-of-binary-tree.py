from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        queue = deque([(1, root)])
        maximum = 1
        while queue:
            curr, node = queue.popleft()
            maximum = max(maximum, curr)
            if node.left:
                queue.append((curr+1, node.left))
            if node.right:
                queue.append((curr+1, node.right))
        return maximum


        # dfs
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return 1 + max(left, right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # maximum = 0
        # current = 0
        # def dfs(node, current):
        #     if not node:
        #         return
        #     current += 1
        #     if not node.left and not node.right:
        #         maximum = max(current, maximum)
        #         return maximum
        #     return dfs(node.left, current) or dfs(node.right, current)
        
        # return dfs(root, 0)

