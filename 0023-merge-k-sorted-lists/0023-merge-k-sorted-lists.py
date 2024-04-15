# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            lists[1] = self.merge(lists[0], lists[1])
            lists.pop(0)
        
        return lists[0]
        
        
        
        
        
    
    
    def merge(self, list1, list2):
        dummy = list3 = ListNode()
        #TODO: optimize me
        while list1 and list2:
            if list1.val > list2.val:
                list3.next = list2
                list2 = list2.next
            else:
                list3.next = list1
                list1 = list1.next
            
            list3 = list3.next
        
        
        list3.next = list1 if list1 else list2
        
        return dummy.next
        
        