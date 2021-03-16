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
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intvls = list()
        for interval in intervals:
            intvls.extend([(interval[0], 'start'), (interval[1], 'end')])
        print(intvls)
        intvls = sorted(intvls, key=lambda x: (x[0], x[1]))
        print(intvls)

        max_concurrent = 0
        concurrent = 0
        for i in intvls:
            if i[1] == 'start':
                concurrent += 1
            else:
                concurrent -= 1
            max_concurrent = max(max_concurrent, concurrent)
        return max_concurrent


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[0,30],[5,10],[15,20]]], 2),
        ([[[7,10],[2,4]]], 1),
        ([[[1,25],[3,50],[26,35],[28,34],[30,37],[31,37],[38,51]]], 5),
        ([[[38,51],[1,25],[3,50],[26,35],[28,34],[30,37],[31,37]]], 5),
        ([[[13,15],[1,13]]], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minMeetingRooms(*input)).run(unordered_output=False)
