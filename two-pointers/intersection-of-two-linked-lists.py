# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        ptr1 = headA
        ptr2 = headB
        set1 = set()
        set2 = set()
        while ptr1 and ptr2:
            if ptr1 in set2:
                return ptr1
            
            set1.add(ptr1)
            
            if ptr2 in set1:
                return ptr2
            
            set2.add(ptr2)

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            if ptr1 in set2:
                return ptr1
            ptr1 = ptr1.next
        
        while ptr2:
            if ptr2 in set1:
                return ptr2
            ptr2 = ptr2.next
        return None
        