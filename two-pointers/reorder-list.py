# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        right = prev
        left = head

        while right:
            nextLeftNode = left.next
            left.next = right
            left = nextLeftNode

            nextRightNode = right.next
            right.next = left
            right = nextRightNode
            
        # if left:
        #     right.next = left
        # if right:
        #     left.next = right
        return head
        
