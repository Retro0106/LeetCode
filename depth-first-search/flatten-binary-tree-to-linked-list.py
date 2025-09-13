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
        if not root:
            return
        # array = []
        # def dfs(node):
        #     if not node:
        #         return
            
            
        #     array.append(node)
        #     dfs(node.left)
        #     dfs(node.right)

        # dummy = TreeNode(0)
        # curr = dummy
        # dfs(root)

        # for node in array:
            
        #     curr.right = node
        #     curr = curr.right
        #     curr.left = None
            
        
        # return dummy.right

        dummy = TreeNode(0)
        stack = [root]
        curr = dummy
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            curr.right = node
            curr.left = None
            curr=curr.right

        return dummy.right