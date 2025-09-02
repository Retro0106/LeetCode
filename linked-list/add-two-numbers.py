# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upper = l1
        lower = l2
        total = upper.val + lower.val
        mod = (total) % 10
        rem = total // 10
        head = ListNode(mod)
        curr = head

        upper = upper.next
        lower = lower.next

        while upper and lower:
            total = rem + upper.val + lower.val
            mod = total % 10
            rem = total // 10
            curr.next = ListNode(mod)
            curr = curr.next
            upper = upper.next
            lower = lower.next
        
        while upper:
            total = rem + upper.val
            mod = total % 10
            rem = total // 10
            curr.next = ListNode(mod)
            curr = curr.next
            upper = upper.next
        
        while lower:
            total = rem + lower.val
            mod = total % 10
            rem = total // 10
            curr.next = ListNode(mod)
            curr = curr.next
            lower = lower.next
        
        if total >= 10 and rem != 0:
            curr.next = ListNode(rem)
            curr = curr.next
        return head


        # first = ''
        # second = ''
        
        # curr_first = l1
        # curr_second = l2

        # while curr_first:
        #     first += str(curr_first.val)
        #     curr_first = curr_first.next
        
        # while curr_second:
        #     second += str(curr_second.val)
        #     curr_second = curr_second.next
        
        
        
        # total = int(first[::-1]) + int(second[::-1])
        # string = str(total)[::-1]

        # head = ListNode(int(string[0]))
        # curr = head

        # for i in range(1, len(string)):
        #     curr.next = ListNode(int(string[i]))
        #     curr = curr.next
        
        # return head


