from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
    #  initialize deque with the root, and result list
    # while deque:
    # initialize a new list
        # for in the range of the length of the deque, 
        # pop from deque and add the left and right of that node if any to deque and list
    # add list to result
    # return result

        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            result.append(curr)
        return result


