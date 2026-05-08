from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root, return 0
        # initialize queue as [(1, root)]
        # set minimum as infinity
        # while queue:
            # for _ in len(queue)
            # pop node and extract current level and node
            # if not node.left and right, minimum = min(minimum, curr)
            # if node.left: add to queue (curr+1, node.left)
            # if node.right: add to queue (curr+1, node.right)
        # return minimum

        if not root: return 0
        queue = deque([(1, root)])
        minimum = float('inf')

        while queue:
            for _ in range(len(queue)):
                curr, node = queue.popleft()
                if not node.left and not node.right:
                    minimum = min(minimum, curr)
                if node.left: queue.append((curr+1, node.left))
                if node.right: queue.append((curr+1, node.right))
        return minimum
















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

        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1

        # # left = right = None
        # if not root.left:
        #     left = None
            
        # else:
        #     left = self.minDepth(root.left)
        
        # if not root.right:
        #     right = None
            
        # else:
        #     right = self.minDepth(root.right)
        
        # if left and not right:
        #     return 1 + left
        
        # if right and not left:
        #     return 1 + right
        
        # return 1 + min(left, right)
