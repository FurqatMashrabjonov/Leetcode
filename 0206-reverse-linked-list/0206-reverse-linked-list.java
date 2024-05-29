/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode prev_ = null;
        
        while (cur != null) {
            ListNode next_ = cur.next;
            cur.next = prev_;
            prev_ = cur;
            cur = next_;
        }
        
        return prev_;
    }
}