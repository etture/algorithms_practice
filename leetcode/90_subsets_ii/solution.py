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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.answer = [[]]
        self.nums = sorted(nums)
        self.run(list(), 0)
        return self.answer

    def run(self, head: List[int], cur_idx: int):
        if cur_idx >= len(self.nums):
            return
        prev_num = -9999
        for idx in range(cur_idx, len(self.nums)):
            n = self.nums[idx]
            if n == prev_num:
                continue
            else:
                prev_num = n
            self.answer.append(head + [n])
            self.run(head + [n], idx + 1)




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,2]], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
        ([[1,2,3]], [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]),
        ([[0]], [[],[0]]),
        ([[1,2,2,3]], [[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]]),
        ([[1,2,2,2]], [[],[1],[1,2],[1,2,2],[1,2,2,2],[2],[2,2],[2,2,2]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.subsetsWithDup(*input)).run(unordered_output=True)
