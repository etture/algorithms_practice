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
# ----------------------------------------------------------
import pprint
pp = pprint.PrettyPrinter()

from math import floor
from random import seed, random
import time

class Solution:

    def __init__(self, w: List[int]):
        self.total = len(w)
        seed(self.total * time.time())

        self.range_list = list()
        self.prefix_sum = 0
        for idx, item in enumerate(w):
            self.prefix_sum += item
            self.range_list.append(self.prefix_sum)
        print(self.range_list)


    def pickIndex(self) -> int:
        random_num = floor(random() * self.prefix_sum) + 1
        print(f'random_num: {random_num}')
        
        # Linear search 
        # for idx, item in enumerate(self.range_list):
        #     if random_num <= item:
        #         return idx

        # Binary search
        left, right = 0, self.total - 1
        while left <= right:
            mid = (left + right) // 2
            # print(f'    left: {left}, mid: {mid}, right: {right}, random_num: {random_num}, compare_to: {self.range_list[mid]}')
            if self.range_list[mid] == random_num:
                return mid
            elif self.range_list[mid] < random_num:
                left = mid + 1
            else:
                if mid == 0:
                    return mid
                else:
                    if self.range_list[mid-1] < random_num:
                        return mid
                    else:
                        right = mid - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        

if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([1,3], 5),
        ([1, 3, 10, 15, 5, 15], 10),
    ]
    
    for idx, case in enumerate(test_cases):
        answer = ['null']
        sol = Solution(case[0])
        for _ in range(case[1]):
            answer.append(sol.pickIndex())
        print(f'Case {idx+1}: {answer}\n')
