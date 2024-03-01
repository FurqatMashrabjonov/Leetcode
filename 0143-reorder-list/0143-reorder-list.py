# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        reversed_arr = list(reversed(arr))
        from_arr = False
        cur = head
        i = 0
        j = 0
        while cur:
            if from_arr:
                cur.val = reversed_arr[i]
                i += 1
            else:
                cur.val = arr[j] 
                j+=1
            from_arr = not from_arr
            cur = cur.next    
        