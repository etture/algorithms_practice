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
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        print(sorted(envelopes, key=lambda x: (x[0], x[1])))
        print(sorted(envelopes, key=lambda x: (x[1], x[0])))

        def linear(_envelopes: List[List[int]]) -> int:
            incr_cnt, max_incr_cnt = 0, 0
            prev_elem = None
            for idx, e in enumerate(_envelopes):
                s = True
                if idx == 0:
                    incr_cnt += 1
                    prev_elem = e
                else:
                    strictly_increasing = e[0] > prev_elem[0] and e[1] > prev_elem[1]
                    s = strictly_increasing
                    if strictly_increasing:
                        incr_cnt += 1
                        prev_elem = e
                max_incr_cnt = max(incr_cnt, max_incr_cnt)
                # print(f'idx: {idx}, e: {e}, s: {s}, incr_cnt: {incr_cnt}, max: {max_incr_cnt}')
            return max_incr_cnt

        return max(linear(sorted(envelopes, key=lambda x: (x[0], x[1]))), linear(sorted(envelopes, key=lambda x: (x[1], x[0]))))


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[5,4],[6,4],[6,7],[2,3]]], 3),
        ([[[1,1],[1,1],[1,1]]], 1),
        ([[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]], 5),
        ([[[46,89],[50,53],[52,68],[72,45],[77,81]]], 3),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxEnvelopes(*input)).run(unordered_output=False)
