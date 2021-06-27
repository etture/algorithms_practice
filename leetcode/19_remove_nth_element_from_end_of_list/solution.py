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

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur_cnt = 0
        cur_node = head
        nodes = list()
        while cur_node is not None:
            nodes.append(cur_node)
            cur_node = cur_node.next
        to_remove_idx = len(nodes) - n
        if to_remove_idx == 0:
            head = head.next
        elif to_remove_idx == len(nodes) - 1:
            nodes[-2].next = None
        else:
            nodes[to_remove_idx - 1].next = nodes[to_remove_idx + 1]
        return head


class Wrapper:
    def __init__(self):
        self.head = None
        self.sol = Solution()

    def setup(self, nodes: List[int]):
        head_node = None
        prev_node, cur_node = None, None
        for idx, node in enumerate(nodes):
            if idx == 0:
                head_node = prev_node = ListNode(val=node)
            else:
                cur_node = ListNode(val=node)
                prev_node.next = cur_node
                prev_node = cur_node
        self.head = head_node

    def solve(self, nodes: List[int], n: int) -> List[int]:
        self.setup(nodes)
        result_head_node: ListNode = self.sol.removeNthFromEnd(self.head, n)
        answer = list()
        cur_node = result_head_node
        while cur_node is not None:
            answer.append(cur_node.val)
            cur_node = cur_node.next
        return answer
        

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



if __name__ == '__main__':
    sol = Wrapper()

    test_cases = [
        ([[1,2,3,4,5], 2], [1,2,3,5]),
        ([[1], 1], []),
        ([[1,2], 1], [1]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solve(*input)).run(unordered_output=False)
