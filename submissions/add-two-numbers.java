// https://leetcode.com/problems/add-two-numbers

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carryOver = 0;
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        while (l1 != null || l2 != null || carryOver > 0){
            int sum = 0;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            sum += carryOver;
            carryOver = sum / 10;
            ListNode node = new ListNode (sum % 10);
            cur.next = node;
            cur = cur.next;
        }

        return dummy.next;

    }
}