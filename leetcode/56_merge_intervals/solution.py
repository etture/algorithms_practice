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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if the intervals are not sorted in ascending order, sort it first
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(intervals)

        # otherwise, proceed
        if len(intervals) <= 1:
            return intervals

        answer_intervals = list()
        cur_intv_first, cur_intv_last = intervals[0]
        
        for intv in intervals:
            if intv[0] >= cur_intv_first and intv[0] <= cur_intv_last:
                if intv[1] >= cur_intv_last:
                    cur_intv_last = intv[1]
            else:
                answer_intervals.append([cur_intv_first, cur_intv_last])
                cur_intv_first, cur_intv_last = intv

        answer_intervals.append([cur_intv_first, cur_intv_last])
        
        return answer_intervals



test_cases = [
    ([[[1,3],[2,6],[8,10],[15,18]]], [[1,6],[8,10],[15,18]]),
    ([[[1,4],[4,5]]], [[1,5]]),
    ([[[2,5],[6,10],[7,10],[8,12],[13,16],[15,16],[16,20],[21,25],[26,30],[27,31]]], [[2,5],[6,12],[13,20],[21,25],[26,31]]),
    ([[[1,2]]], [[1,2]]),
    ([[[1,4],[0,4]]], [[0,4]]),
    ([[[1,4],[2,3]]], [[1,4]]),
    ([[[2,4],[1,9]]], [[1,9]]),
    ([[[2,4],[3,4],[5,7],[7,8],[7,8],[7,9],[1,8],[3,8],[1,9]]], [[1,9]]),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.merge(*input)).run(unordered_output=False)
