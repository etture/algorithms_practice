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
        # print(f'input: {w}')

        # self.w = w
        # self.probability_map = dict()
        self.total = sum(w)

        # val = 0
        # for idx, item in enumerate(w):
        #     for _ in range(item):
        #         self.probability_map[val] = idx
        #         val += 1

        seed(self.total * time.time())


        self.range_list = list()
        cnt = 0
        for idx, item in enumerate(w):
            cnt += item
            self.range_list.append(tuple([cnt, idx]))
        # print(self.range_list)


    def pickIndex(self) -> int:
        random_num = floor(random() * self.total) + 1
        # print(f'map: {self.probability_map}, random_num: {random_num} -> index: {self.probability_map[random_num]}')
        # return self.probability_map[random_num]

        # print(f'random_num: {random_num}')
        for item in self.range_list:
            if random_num <= item[0]:
                return item[1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        

if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([1,3], 5),
    ]
    
    for idx, case in enumerate(test_cases):
        answer = ['null']
        sol = Solution(case[0])
        for _ in range(case[1]):
            answer.append(sol.pickIndex())
        print(f'Case {idx+1}: {answer}\n')
