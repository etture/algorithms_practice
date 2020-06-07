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
logger = Logger(verbose=True)                             
# ----------------------------------------------------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def setup(self, l1: List[int], l2: List[int]):
        prev_node = None
        l1_head = None
        for num in l1:
            node = ListNode(num)
            if prev_node:
                prev_node.next = node
            else:
                l1_head = node
            prev_node = node

        prev_node = None
        l2_head = None
        for num in l2:
            node = ListNode(num)
            if prev_node:
                prev_node.next = node
            else:
                l2_head = node
            prev_node = node


        answer = self.mergeTwoLists(l1_head, l2_head)
        return_val = [answer.val]
        while answer.next:
            answer = answer.next
            return_val.append(answer.val)
        return return_val

    def setup_answer(self, ll):
        prev_node = None
        l1_head = None
        for num in ll:
            node = ListNode(num)
            if prev_node:
                prev_node.next = node
            else:
                l1_head = node
            prev_node = node
        return l1_head


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root_node = None
        cur_node = None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    if cur_node:
                        cur_node.next = l1
                        cur_node = cur_node.next
                    else:
                        root_node = l1
                        cur_node = root_node
                    l1 = l1.next
                else:
                    if cur_node:
                        cur_node.next = l2
                        cur_node = cur_node.next
                    else:
                        root_node = l2
                        cur_node = root_node
                    l2 = l2.next
            elif l1:
                if cur_node:
                    cur_node.next = l1
                    cur_node = cur_node.next
                else:
                    root_node = l1
                    cur_node = root_node
                l1 = l1.next
            else:
                if cur_node:
                    cur_node.next = l2
                    cur_node = cur_node.next
                else:
                    root_node = l2
                    cur_node = root_node
                l2 = l2.next
        return root_node


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([[1,2,4], [1,3,4]], [1,1,2,3,4,4])
]

solution = Solution().setup

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
