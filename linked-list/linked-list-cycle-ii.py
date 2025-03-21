# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        if not head:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   

            if slow == fast:
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
        
        
        
        
        # slow = head
        # hashset = set() 
        # if not head:
        #     return None
        # while slow:
        #     if slow in hashset:
        #         return slow
        #     hashset.add(slow)
        #     slow = slow.next
        # return None


            