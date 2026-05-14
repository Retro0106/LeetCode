from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # if not root: return []
        # initialize empty list, queue as deque
        # while queue
        # get length of queue and intiaitilaize total as 0
        # for _ in range of queue
            # pop node, add it to total
            # if node.left, if node.right
        # add average(total/length) to result list
        # return result

        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            length = len(queue)
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(total / length)
        return result