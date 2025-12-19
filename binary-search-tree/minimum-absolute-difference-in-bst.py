# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # if leaf node: return infinity
        # each node would return ints MAD
        # for each root, return minimum of node.left MAD, node.right MAD, abs(node-node.left), abs(node-node.right)
        
        if not root:
            return float('inf')
        
        if not root.left and not root.right:
            return float('inf')
        left = right = float('inf')
        if root.left:
            left = root.left.val
        
        if root.right:
            right = root.right.val

        return min(self.getMinimumDifference(root.left), abs(root.val-left), abs(root.val-right),self.getMinimumDifference(root.right))
        