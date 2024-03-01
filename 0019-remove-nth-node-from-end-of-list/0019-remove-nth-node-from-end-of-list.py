# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        dummy = prev = ListNode
        cur = head
        while length != n:
            prev.next = cur
            cur = cur.next
            prev = prev.next
            length -= 1
        prev.next = cur.next

        return dummy.next