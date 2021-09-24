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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        _head = None
        left_last = None
        right_first = None

        cur_node = head
        prev_node = None
        while cur_node:
            if _head is None:
                _head = cur_node
            elif cur_node.val < x:
                if right_first is None:  # means don't have to move left
                    left_last = cur_node
                    prev_node = cur_node
                    cur_node = cur_node.next
                else:
                    prev_node.next = cur_node.next
                    cur_node.next = right_first
                    if left_last is None:  # first left occurrence
                        left_last = cur_node
                        _head = cur_node
                    else:  # there's already left
                        left_last.next = cur_node
                        left_last = cur_node
                    cur_node = prev_node.next
            else:
                if right_first is None:
                    right_first = cur_node
                prev_node = cur_node
                cur_node = cur_node.next
        
        return _head


class Wrapper:
    def solve(self, nodes: List[int], x: int) -> Optional[ListNode]:
        head = None
        cur = None
        for n in nodes:
            node = ListNode(val=n)
            if head is None:
                head = node
            else:
                cur.next = node
            cur = node
        
        sol = Solution()
        answer = sol.partition(head, x)
        answer_list = list()
        while answer:
            answer_list.append(answer.val)
            answer = answer.next
        return answer_list
        


if __name__ == '__main__':
    sol = Wrapper()

    test_cases = [
        ([[1,4,3,2,5,2], 3], [1,2,2,4,3,5]),
        ([[2,1], 2], [1,2]),
        ([[2,1,1,4,3,2,5,2], 3], [2,1,1,2,2,4,3,5]),
        ([[4,3,2,5,2], 3], [2,2,4,3,5]),
        ([[4,3,5], 3], [4,3,5]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solve(*input)).run(unordered_output=False)
