# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'val: {self.val}'

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        lenA = self.getListLength(headA)
        lenB = self.getListLength(headB)
        combinedLen = lenA + lenB
        print(f'lenA: {lenA}, lenB: {lenB}')
        
        pntA = headA
        pntB = headB

        if pntA == pntB:
            return pntA
        for i in range(combinedLen):
            if pntA.next is not None:
                pntA = pntA.next
            else:
                pntA = headB
            if pntB.next is not None:
                pntB = pntB.next
            else:
                pntB = headA
            if pntA == pntB:
                return pntA
        return None
            
    def getListLength(self, head: ListNode) -> int:
        length = 1
        pnt = head
        while pnt.next is not None:
            pnt = pnt.next
            length += 1
        return length


if __name__ == '__main__':
    solution = Solution()

    a_node1 = ListNode(4)
    a_node2 = ListNode(1)
    a_node3 = ListNode(8)
    a_node4 = ListNode(4)
    a_node5 = ListNode(5)

    b_node1 = ListNode(5)
    b_node2 = ListNode(6)
    b_node3 = ListNode(1)

    a_node1.next = a_node2
    a_node2.next = a_node3
    a_node3.next = a_node4
    a_node4.next = a_node5

    b_node1.next = b_node2
    b_node2.next = b_node3
    b_node3.next = a_node3

    print(solution.getIntersectionNode(a_node1, b_node1))
