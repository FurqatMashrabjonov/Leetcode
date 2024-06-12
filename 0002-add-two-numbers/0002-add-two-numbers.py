# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        prefix = 0
        while l1 or l2:
            cur.next = ListNode()
            cur = cur.next
            sum_ = prefix
            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            cur.val = sum_ % 10
            prefix = sum_ // 10
        
        if prefix != 0:
            cur.next = ListNode(prefix)
        
        return dummy.next