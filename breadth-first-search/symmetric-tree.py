from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # initialize queue with just root
        # while queue:
            # initialize left and right pointers
            # loop through while left < right if left.val != right.val, return False
            # loop for _ in range of length of queue:
                # node popleft
                # add children if any
        # return true

        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)   
                    queue.append(node.right)
                else:
                    level.append(None) 

            left, right = 0, len(level) - 1
            while left < right:
                if level[left] != level[right]:
                    return False
                left += 1
                right -= 1

        return True
    
  