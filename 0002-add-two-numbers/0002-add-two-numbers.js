/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let head = new ListNode();
    let res = head;
    let tmp = 0
    while(l1 || l2){
   
        if (l1){
            res.val += l1.val
            l1 = l1.next
        }
         if (l2){
            res.val += l2.val
             l2 = l2.next
         }
        res.val += tmp
        if (res.val >= 10){
            res.val %= 10
            tmp = 1
        }else {
            tmp = 0
        }
       if (l1 || l2){
        res.next = new ListNode()
        res = res.next
       }
    }
    if (tmp !== 0){
        res.next = new ListNode()
        res.next.val = tmp
    }
    return head
};