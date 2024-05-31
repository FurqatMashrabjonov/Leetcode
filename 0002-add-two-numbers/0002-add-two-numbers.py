# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode(0)
        prefix = 0
        prev = None
        while head1 or head2:
            sum_ = prefix 
            if head1:
                sum_ += head1.val
                head1 = head1.next
            if head2:
                sum_ += head2.val
                head2 = head2.next


            res.val = sum_ % 10
            prefix = sum_ // 10
            res.next = ListNode(0)
            prev = res
            res = res.next

        if prefix != 0:
            res.val = prefix
        else:
            prev.next = None


        return dummy