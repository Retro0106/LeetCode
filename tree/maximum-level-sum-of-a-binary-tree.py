# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # if not root: return none
        # initialize queue, curr_maximum as neg infinity, i as 1, level as none
        # while queue:
            # initialize a total as 0
            # for _ in range(queue)
                # pop node and add to total
                # if node.left, right, add
            # if total > curr_maximum, level = i, curr_maximum = total
            # i += 1
        # return level

        if not root: return None
        queue = deque([root])
        curr_max = float('-inf')
        i = 1
        level = None
        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if total > curr_max: 
                level = i
                curr_max = total
            i += 1
        return level

