from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        result = [[root.val]]
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                result.append([node.left.val, node.right.val])
                queue.append(node.left)
                queue.append(node.right)
            elif node.left:
                result.append([node.left.val])
                queue.append(node.left)
            elif node.right:
                result.append([node.right.val])
                queue.append(node.right)
        return result