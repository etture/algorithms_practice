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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recurse(counted: Set[tuple], prev_combo: List[int], prev_sum: int):
            for i in range(len(candidates)):
                cur_combo = [a for a in prev_combo]
                if prev_sum + sorted_candidates[i] == target:
                    cur_combo[i] += 1
                    combination = list()
                    for idx, elem in enumerate(cur_combo):
                        for _ in range(elem):
                            combination.append(sorted_candidates[idx])
                    # print(f'match -> {combination}, prev_sum: {prev_sum}, candidates[i]: {sorted_candidates[i]}')
                    counted.add(tuple(combination))
                elif prev_sum + sorted_candidates[i] < target:
                    cur_combo[i] += 1
                    recurse(counted, cur_combo, prev_sum + sorted_candidates[i])
    
        sorted_candidates = sorted(candidates)
        counted_set = set()
        recurse(counted_set, [0 for _ in sorted_candidates], 0)
        return list([list(x) for x in counted_set])



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,3,6,7], 7], [[2,2,3],[7]]),
        ([[2,3,5], 8], [[2,2,2,2],[2,3,3],[3,5]]),
        ([[2], 1], []),
        ([[1], 1], [[1]]),
        ([[1], 2], [[1,1]]),
        ([[2,7,6,3,5,1], 9], [[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2],[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],[1,1,1,6],[1,1,2,2,3],[1,1,2,5],[1,1,7],[1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.combinationSum(*input)).run(unordered_output=True)
