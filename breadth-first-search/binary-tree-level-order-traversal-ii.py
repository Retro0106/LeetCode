from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root return none
        # initialize queue with root, empty queue
        # while queue:
            # initialize list
            # for _ in range(len(deque))
                # pop node and add to list
                # if node.left, add to queue, same for right
            # appendleft list to queue 2
        # convert queue 2 to list and return it
        if not root:
            return []
        queue = deque([root])
        result = deque([])

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.appendleft(curr)
        return list(result)