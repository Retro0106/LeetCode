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
        self.arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        minimum = float('inf')
        if len(self.arr) < 2:
            return 0
        for i in range(1, len(self.arr)):
            minimum = min(minimum, self.arr[i]-self.arr[i-1])
        return minimum

















        # if not root:
        #     return float('inf')
        
        # if not root.left and not root.right:
        #     return float('inf')
        # left = right = float('inf')
        # if root.left:
        #     left = root.left.val
        
        # if root.right:
        #     right = root.right.val

        # return min(self.getMinimumDifference(root.left), abs(root.val-left), abs(root.val-right),self.getMinimumDifference(root.right))
        