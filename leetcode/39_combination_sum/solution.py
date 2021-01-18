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

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global_answer = list()
        for idx, cand in enumerate(candidates):
            self.recurse(candidates[idx:], [cand], cand, target, global_answer)
        return global_answer

    def recurse(self, pool: List[int], cur_comb: List[int], cur_sum: int, target: int, global_answer: List[List[int]]):
        # print(f'pool: {pool}, cur_comb: {cur_comb}, target: {target}')
        if cur_sum > target:
            return
        if cur_sum == target:
            global_answer.append(cur_comb)
            return
        for idx, x in enumerate(pool):
            self.recurse(pool[idx:], cur_comb + [x], cur_sum + x, target, global_answer)
        


test_cases = [
    ([[2,3,6,7], 7], [[2,2,3],[7]]),
    ([[2,3,5], 8], [[2,2,2,2],[2,3,3],[3,5]]),
    ([[2], 1], []),
    ([[1], 1], [[1]]),
    ([[1], 2], [[1,1]]),
    ([[2,3,5], 9], [[2,2,2,3],[3,3,3],[2,2,5]]),
]

if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.combinationSum(*input)).run(unordered_output=True)
