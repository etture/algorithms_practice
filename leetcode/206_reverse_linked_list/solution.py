# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 
# 파이썬 기본 재귀 limit이 1000이라고 함 --> 10^6으로 manual하게 설정
sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
import pprint
pp = pprint.PrettyPrinter()
# ----------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        # iterative solution
        # cur_node = head
        # prev_node = None
        # while True:
        #     next_node = cur_node.next
        #     if prev_node is None:
        #         cur_node.next = None
        #     else:
        #         cur_node.next = prev_node
        #     prev_node = cur_node
        #     if next_node is None:
        #         return cur_node
        #     cur_node = next_node

        # recursive solution
        def recurse(node: ListNode) -> ListNode:
            new_head = None
            if node.next is not None:
                new_head = recurse(node.next)
                node.next.next = node
                node.next = None
            if new_head is None:
                new_head = node
            return new_head
        return recurse(head)
            



class Wrapper:
    def __init__(self):
        self.solution = Solution()

    def node_to_list(self, head: ListNode) -> List[int]:
        answer = list()
        cur_node = head
        while cur_node is not None:
            answer.append(cur_node.val)
            cur_node = cur_node.next
        return answer

    def solve(self, input: List[int]) -> List[int]:
        head_node = None
        cur_node = None
        for num in input:
            new_node = ListNode(val=num)
            if head_node is None:
                head_node = new_node
            if cur_node is not None:
                cur_node.next = new_node
            cur_node = new_node

        return self.node_to_list(self.solution.reverseList(head_node))


if __name__ == '__main__':
    sol = Wrapper()

    test_cases = [
        ([[1,2,3,4,5]], [5,4,3,2,1]),
        ([[1,2]], [2,1]),
        ([[]], []),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solve(*input)).run(unordered_output=False)
