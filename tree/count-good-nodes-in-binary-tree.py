# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maximum):
            if not node:
                return 0
            
            left = dfs(node.left, max(maximum, node.val))
            right = dfs(node.right, max(maximum, node.val))
            ans = left + right
            if node.val >= maximum:
                ans += 1
            
            
            
            
            return ans

        return dfs(root, float('-inf'))
        





        # def dfs(node, maximum):
        #     nonlocal count
        #     if not node:
        #         return 
            
        #     if node.val >= maximum:
        #         count += 1
        #     maximum = max(maximum, node.val)
            
        #     dfs(node.left, maximum)
        #     dfs(node.right, maximum)
            
        # dfs(root, float('-inf'))
        # return count