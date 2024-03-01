# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = newNode = ListNode()
        
        while True:
            minIndex = 0
            minValue = float('inf')
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                    
                if lists[i].val < minValue:
                    minValue = lists[i].val
                    minIndex = i
            if minValue == float('inf'):
                break
            tmp = ListNode(minValue)
            newNode.next = tmp
            newNode = newNode.next
            lists[minIndex] = lists[minIndex].next
        
        return dummy.next
        