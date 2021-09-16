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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        print(f'sorted_candidates: {sorted_candidates}')
        
        def recurse(pool: List[int], prev_comb: List[int], prev_sum: int, answers: Set[tuple[int]]):
            prev_num = -1
            for idx, num in enumerate(pool):
                if num == prev_num: continue
                prev_num = num
                if prev_sum + num == target:
                    answers.add(tuple(sorted(prev_comb + [num])))
                elif prev_sum + num < target:
                    recurse(pool[idx+1:], prev_comb + [num], prev_sum + num, answers)

        answers_set = set()
        recurse(sorted_candidates, list(), 0, answers_set)
        return list([list(x) for x in answers_set])
        




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[10,1,2,7,6,1,5], 8], [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([[2,5,2,1,2], 5], [[1,2,2],[5]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.combinationSum2(*input)).run(unordered_output=True)
