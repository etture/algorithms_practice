/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; next = null; } }
 */

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        int lenA = getListLength(headA);
        int lenB = getListLength(headB);
        int combinedLen = lenA + lenB;

        if (headA == headB) return headA;
        ListNode pntA = headA;
        ListNode pntB = headB;
        for (int i = 0; i < combinedLen; i++) {
            if (pntA.next != null) pntA = pntA.next;
            else pntA = headB;

            if (pntB.next != null) pntB = pntB.next;
            else pntB = headA;

            if (pntA == pntB) return pntA;
        }
        return null;
    }

    int getListLength(ListNode head) {
        int cnt = 1;
        while (head.next != null) {
            head = head.next;
            cnt += 1;
        }
        return cnt;
    }

    public static void main(String[] args) {
        ListNode aNode1 = new ListNode(4);
        ListNode aNode2 = new ListNode(1);
        ListNode aNode3 = new ListNode(8);
        ListNode aNode4 = new ListNode(4);
        ListNode aNode5 = new ListNode(5);

        ListNode bNode1 = new ListNode(5);
        ListNode bNode2 = new ListNode(6);
        ListNode bNode3 = new ListNode(1);

        aNode1.next = aNode2;
        aNode2.next = aNode3;
        aNode3.next = aNode4;
        aNode4.next = aNode5;

        bNode1.next = bNode2;
        bNode2.next = bNode3;
        bNode3.next = aNode3;

        Solution solution = new Solution();
        ListNode answer = solution.getIntersectionNode(aNode1, bNode1);
        System.out.println(answer.val);
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}
