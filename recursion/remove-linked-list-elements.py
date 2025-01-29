# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        ptr = head
        while ptr and ptr.val == val:
            ptr = ptr.next
        
        if not ptr:
            return None
        newHead = ptr

        while ptr and ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            ptr = ptr.next 
        
        return newHead