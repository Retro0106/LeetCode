# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        if not head or not head.next:
            return head
        while curr.next:
            if curr.next.val == val:
                prev = curr
                curr = curr.next
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
                if curr:
                    curr = curr.next
                else:
                    break
            else:
                curr = curr.next
        return dummy.next