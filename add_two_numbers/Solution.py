# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        res = ListNode(0, None)
        pres = res
        over = False
        while l1 or l2:
            if not l1:
                l1 = ListNode(0, None)
            if not l2:
                l2 = ListNode(0, None)    
            cur = l1.val + l2.val
            cur += 1 if over else 0
            if cur > 9:
                over = True
            else:
                 over = False
            digit = cur % 10
            pres.next = ListNode(digit, None)
            pres = pres.next
            l1, l2 = l1.next, l2.next

        if over:
            pres.next = ListNode(1, None)
        return res.next