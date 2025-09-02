# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ''
        second = ''
        
        curr_first = l1
        curr_second = l2

        while curr_first:
            first += str(curr_first.val)
            curr_first = curr_first.next
        
        while curr_second:
            second += str(curr_second.val)
            curr_second = curr_second.next
        
        
        
        total = int(first[::-1]) + int(second[::-1])
        string = str(total)[::-1]

        head = ListNode(int(string[0]))
        curr = head

        for i in range(1, len(string)):
            curr.next = ListNode(int(string[i]))
            curr = curr.next
        
        return head


