# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # METHOD I: O(n), O(n)
        # hashSet = set()
        # ptr = head
        # temp = head
        # while ptr:

        #     if ptr.val in hashSet:
        #         temp.next = ptr.next
        #         ptr = temp.next
            
        #     else:
        #         hashSet.add(ptr.val)
        #         temp = ptr
        #         ptr = ptr.next
        
        # return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
