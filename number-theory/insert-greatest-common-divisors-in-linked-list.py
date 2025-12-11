# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(num1, num2):
            minimum = min(num1, num2)
            maximum = max(num1, num2)
            for num in range(minimum, 0, -1):
                if maximum % num == 0 and minimum % num == 0:
                    return num
        
        curr = head
        while curr and curr.next:
            next_node = curr.next
            new_node = ListNode(gcd(curr.val, next_node.val))
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
        return head

        