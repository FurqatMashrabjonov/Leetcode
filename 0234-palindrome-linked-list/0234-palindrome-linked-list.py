# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = slow 
        slow = slow.next 
        prev.next = None
        
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True