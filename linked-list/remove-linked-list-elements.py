# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # if not head or head.val == val, return None
        # initialize dummy node, dummy.next = head
        # initialize curr as head
        # while curr and curr.next
            # if curr.enxt.val == val; curr.next = curr.next.next
            # else: curr = curr.next
        
        # return dummy.next

        if not head: return None
        dummy = ListNode(next=head)
        curr = dummy
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else: 
                curr = curr.next
        return dummy.next