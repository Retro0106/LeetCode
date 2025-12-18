# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            left = None
        else:
            left = self.maxDepth(root.left)
        
        if not root.right:
            right = None
        else:
            right = self.maxDepth(root.right)
        
        if left and not right:
            return 1 + left
        elif right and not left:
            return 1 + right
        return 1 + max(left, right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

