# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        base_node = ListNode((node1.val + node2.val) % 10)
        cur_node = base_node
        carry = 1 if node1.val + node2.val >= 10 else 0
        while node1.next is not None and node2.next is not None:
            node1 = node1.next
            node2 = node2.next
            sum = node1.val + node2.val + carry
            new_node = ListNode(sum % 10)
            carry = 1 if sum >= 10 else 0
            cur_node.next = new_node
            cur_node = new_node

        if node1.next is None:
            remaining_node = node2
        else:
            remaining_node = node1

        while remaining_node.next is not None:
            working_node = remaining_node.next

            if working_node.val + carry >= 10:
                working_node.val = 0
                carry = 1
            else:
                working_node.val += carry
                carry = 0

            remaining_node = working_node
            cur_node.next = working_node
            cur_node = working_node

        if carry == 1:
            highest_digit = ListNode(1)
            cur_node.next = highest_digit

        return base_node


def print_linked_list(list: ListNode):
    node: ListNode = list
    to_print = [list.val]
    while node.next is not None:
        node = node.next
        to_print.append(node.val)
    print(' -> '.join('{0}'.format(n) for n in to_print))


if __name__ == "__main__":
    solution = Solution()
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    # l1_3 = ListNode(3)
    l1_1.next = l1_2
    # l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(8)
    l2_1.next = l2_2
    l2_2.next = l2_3
    print_linked_list(solution.addTwoNumbers(l1_1, l2_1))
