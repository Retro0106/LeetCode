# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        array = []
        def dfs(node):
            if not node:
                return
            
            nonlocal array
            array.append(node)
            dfs(node.left)
            dfs(node.right)

        dummy = TreeNode(0)
        curr = dummy
        dfs(root)

        for node in array:
            curr.left = None
            curr.right = node
            curr = curr.right
            
        
        return dummy.right