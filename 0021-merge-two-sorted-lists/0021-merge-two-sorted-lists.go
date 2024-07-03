/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
    res := dummy
    
    for list1 != nil && list2 != nil {
        if list1.Val > list2.Val {
            res.Next = list2
            list2 = list2.Next
        }else {
            res.Next = list1
            list1 = list1.Next
        }
        
        res = res.Next            
        
    }
    
    if list1 != nil {
        res.Next = list1
    }
    
    if list2 != nil {
        res.Next = list2
    }

    
    return dummy.Next
}