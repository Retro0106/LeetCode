from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1:
                return False
            if not node2:
                return False

            if node1.val != node2.val:
                return False
            

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(p,q)

        # initialize deque, and result list with root p and q
        # while queue,
            # initialize curr = []
            # for _ in range of len(queue)
                # pop from queue, add to curr
        # compare that theyre both empty

        # queue_p = deque([p])
        # queue_q = deque([q])

        # while queue_p and queue_q:
        #     n1 = queue_p.popleft()
        #     n2 = queue_q.popleft()

        #     if not n1 and not n2:
        #         continue

        #     if not n1 or not n2 or n1.val != n2.val:
        #         return False

        #     queue_p.append(n1.left)
        #     queue_p.append(n1.right)

        #     queue_q.append(n2.left)
        #     queue_q.append(n2.right)

        # return not queue_p and not queue_q

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        

        
    
