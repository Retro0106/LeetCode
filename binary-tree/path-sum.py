from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if not root: return false
        # initialize queue with (0, root node)
        # while queue:
            # for _ in range of len of queue
                # pop curr sum and node
                # update curr sum
                # if node is a leaf, check if curr sum  == target Sum. if so return True
                # if node.left: add to queue as (curr_sum, node.left)
                # if node.right: add to queue as (curr_sum, node.right)
        # return False

        if not root: return False
        queue = deque([(0, root)])
        while queue:
            for _ in range(len(queue)):
                curr_sum, node = queue.popleft()
                curr_sum += node.val
                if not node.left and not node.right:
                    if curr_sum == targetSum:
                        return True
                if node.left: queue.append((curr_sum, node.left))
                if node.right: queue.append((curr_sum, node.right))
        return False

        








        # def dfs(node, curr):
        #     if not node:
        #         return False
            
        #     curr += node.val
        #     if not node.left and not node.right:
        #         return curr == targetSum
            
        #     return dfs(node.left, curr) or dfs(node.right, curr)
                    
            
        
        # return dfs(root, 0)
