from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # if depth is 1, create newRoot and set previous root as its left  then return it
        # initialize queue as deque with (1, root)
        # while queue:
            # for _ in range(len(queue)):
                # pop node, check if its depth = depth - 1
                    # if it is: create 2 nodes(left and right node)
                        # leftnode.left = curr.left, rightnode.right = curr.right; curr.left = leftnode, curr.right = rightnode
                # if add curr.left to queue, curr.right to queue
        # return root

        if depth == 1:
            newRoot = TreeNode(val, left = root)
            return newRoot
        
        queue = deque([(1, root)])
        while queue:
            for _ in range(len(queue)):
                curr_depth, node = queue.popleft()
                if curr_depth == depth - 1:
                    leftNode = TreeNode(val, left = node.left)
                    rightNode = TreeNode(val, right = node.right)

                    node.left = leftNode
                    node.right = rightNode
                if node.left: queue.append((curr_depth + 1, node.left))
                if node.right: queue.append((curr_depth + 1, node.right))
        return root
                    
