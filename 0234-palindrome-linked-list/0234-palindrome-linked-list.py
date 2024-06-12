# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        second = slow
        
        p = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        
        first = head
        
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        
        return True
        
        
        