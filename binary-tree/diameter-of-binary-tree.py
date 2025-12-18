# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # get no of nodes of left
        # get no of nodes of right
        # keep track of max diameter(left + right)
        # return max(left, right)
        self.maximum = 0
        def dfs(node):
            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            self.maximum = max(self.maximum, diameter)
            return 1 + max(left, right)
        
        dfs(root)
        return self.maximum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_diameter = 0
        
        # def dfs(node):
        #     if not node:
        #         return 0

        #     height_left = dfs(node.left)
        #     height_right = dfs(node.right)

        #     nonlocal max_diameter
        #     max_diameter = max(max_diameter, height_left + height_right)

        #     return 1 + max(height_left, height_right)
        
        # dfs(root)
        # return max_diameter

    
    
        
            


       
       








    
