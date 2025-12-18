# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
                return 0
        def dfs(node):
            if not node.left and not node.right:
                return (0, node.val, node.val)
            
            left = right = None
            if node.left:
                left = dfs(node.left)
            
            if node.right:
                right = dfs(node.right)
            
            if left and right:
                curr = max(left[0],abs(node.val-left[1]), abs(node.val-left[2]), abs(node.val-right[1]), abs(node.val-right[2]), right[0])
                minimum = min(left[1], node.val, right[1])
                maximum = max(left[2], node.val, right[2])

                
            
            elif left:
                curr = max(left[0],abs(node.val-left[1]), abs(node.val-left[2]))
                minimum = min(left[1], node.val)
                maximum = max(left[2], node.val)
            
            elif right:
                curr = max(right[0],abs(node.val-right[1]), abs(node.val-right[2]))
                minimum = min(right[1], node.val)
                maximum = max(right[2], node.val)
            
            return (curr, minimum, maximum)
            
        
        curr, minimum, maximum = dfs(root)
        return curr