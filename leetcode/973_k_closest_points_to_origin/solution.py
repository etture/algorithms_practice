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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_calculated = list()
        for p in points:
            square_sum = p[0]**2 + p[1]**2
            distance_calculated.append((p, square_sum))
        return [x[0] for x in sorted(distance_calculated, key=lambda x: x[1])[:k]]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,3],[-2,2]], 1], [[-2,2]]),
        ([[[3,3],[5,-1],[-2,4]], 2], [[3,3],[-2,4]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.kClosest(*input)).run(unordered_output=True)
