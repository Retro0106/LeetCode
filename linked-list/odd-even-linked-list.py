# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # set curr as head, second as curr.next, store second head
        # while curr.next and second.next:
            # curr.next = second.next, curr = curr.next
            # second.next = curr.next, second = second.next

        # curr.next = second_head
        # return head

        curr = head
        head2 = curr.next
        second = curr.next
        while curr.next and second.next:
            curr.next = second.next
            curr = curr.next
            second.next = curr.next
            second = second.next
        curr.next = head2
        
        return head