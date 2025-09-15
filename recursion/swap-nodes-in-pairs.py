# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        curr = head

        if not head or not head.next:
            return head
        


        while curr and curr.next:
            nextNode = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = nextNode
            prev = curr
            curr = curr.next
        
        return dummy.next