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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = [[]]
        self.nums = nums
        self.run([], 0)
        return self.answer

    def run(self, head: List[int], cur_idx: int):
        if cur_idx >= len(self.nums):
            return
        for idx in range(cur_idx, len(self.nums)):
            n = self.nums[idx]
            self.answer.append(head + [n])
            self.run(head + [n], idx + 1)



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3]], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([[0]], [[],[0]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.subsets(*input)).run(unordered_output=True)
