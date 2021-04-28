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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_cur, l2_cur = l1, l2
        carry = 0
        answer_head = None
        answer_cur = None
        while not (l1_cur is None and l2_cur is None):
            l1_val = l1_cur.val if l1_cur is not None else 0
            l2_val = l2_cur.val if l2_cur is not None else 0
            cur_sum = l1_val + l2_val + carry
            # print(f'l1_val: {l1_val}, l2_val: {l2_val}, cur_sum: {cur_sum}')
            if cur_sum >= 10:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0
            new_node = ListNode(cur_sum)
            if answer_head is None:
                answer_head = new_node
                answer_cur = new_node
            else:
                answer_cur.next = new_node
                answer_cur = new_node
            if l1_cur is not None:
                l1_cur = l1_cur.next
            if l2_cur is not None:
                l2_cur = l2_cur.next
        if carry > 0:
            answer_cur.next = ListNode(1)
        return answer_head
    

class Problem:
    def solve(self, l1: List[int], l2: List[int]):
        l1_head = ListNode(l1[0])
        l1_cur = l1_head
        for idx in range(1, len(l1)):
            node = ListNode(l1[idx])
            l1_cur.next = node
            l1_cur = node
        
        l2_head = ListNode(l2[0])
        l2_cur = l2_head
        for idx in range(1, len(l2)):
            node = ListNode(l2[idx])
            l2_cur.next = node
            l2_cur = node

        sol = Solution()
        answer_node = sol.addTwoNumbers(l1_head, l2_head)
        answer_list = list()
        while answer_node is not None:
            answer_list.append(answer_node.val)
            answer_node = answer_node.next
        return answer_list

if __name__ == '__main__':
    test_cases = [
        ([[2,4,3],[5,6,4]], [7,0,8]),
        ([[0],[0]], [0]),
        ([[9,9,9,9,9,9,9],[9,9,9,9]], [8,9,9,9,0,0,0,1]),
    ]

    prob = Problem()

    Tester.factory(test_cases, func=lambda input: prob.solve(*input)).run(unordered_output=False)
