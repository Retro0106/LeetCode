# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(node, curr):
            if not node:
                return False
            if node.left == None and node.right == None:
                return curr + node.val == targetSum
            
            curr += node.val
            if curr > targetSum:
                return False
            if curr == targetSum:
                return True
            return dfs(node.left, curr) or dfs(node.right, curr)
        
        return dfs(root, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(node, curr):
        #     if not node:
        #         return False
            
        #     curr += node.val
        #     if not node.left and not node.right:
        #         return curr == targetSum
            
        #     return dfs(node.left, curr) or dfs(node.right, curr)
                    
            
        
        # return dfs(root, 0)
