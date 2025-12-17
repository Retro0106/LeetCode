# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)

        # if left == 0:
        #     return 1 + right
        # elif right == 0:
        #     return 1 + left

        # return 1 + min(left, right)

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # left = right = None
        if not root.left:
            left = None
            
        else:
            left = self.minDepth(root.left)
        
        if not root.right:
            right = None
            
        else:
            right = self.minDepth(root.right)
        
        if left:
            return 1 + left
        
        if right:
            return 1 + right
        
        return 1 + min(left, right)
