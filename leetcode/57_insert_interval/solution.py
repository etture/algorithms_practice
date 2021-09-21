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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        self.intervals = intervals
        self.MIN, self.MAX = -1, 99999999

        left_res = self.binary_search(newInterval[0], left_pos=True)
        right_res = self.binary_search(newInterval[1], left_pos=False)
        left_idx = left_res if left_res is not None else self.MIN
        right_idx = right_res if right_res is not None else self.MAX

        print(f'left_idx: {left_idx}, right_idx: {right_idx}')

        if left_idx == self.MIN:
            if right_idx == self.MIN:
                return [newInterval] + intervals
            if right_idx == self.MAX:
                return [newInterval]
            return [[newInterval[0], max(intervals[right_idx][1], newInterval[1])]] + intervals[right_idx+1:]
        if right_idx == self.MAX:
            if left_idx == self.MAX:
                return intervals + [newInterval]
            return intervals[:left_idx] + [[min(intervals[left_idx][0], newInterval[0]), newInterval[1]]]
        return intervals[:left_idx] + [[min(intervals[left_idx][0], newInterval[0]), max(intervals[right_idx][1], newInterval[1])]] + intervals[right_idx+1:]

        
    def binary_search(self, target_num: int, left_pos: bool) -> int:
        left, right = 0, len(self.intervals) - 1
        middle = 0
        while left <= right:
            middle = (left + right) // 2
            target_interval = self.intervals[middle]
            if target_interval[0] <= target_num <= target_interval[1]:
                return middle
            elif target_num < target_interval[0]:
                right = middle - 1
            else:
                left = middle + 1
    
        if left >= len(self.intervals):
            return self.MAX
        elif right < 0:
            return self.MIN
        else:
            if left_pos:
                return left
            else:
                return right



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,3],[6,9]], [2,5]], [[1,5],[6,9]]),
        ([[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]], [[1,2],[3,10],[12,16]]),
        ([[[1,2],[3,5],[6,7],[9,10],[12,16]], [4,8]], [[1,2],[3,8],[9,10],[12,16]]),
        ([[], [5,7]], [[5,7]]),
        ([[[1,5]], [2,3]], [[1,5]]),
        ([[[1,5]], [2,7]], [[1,7]]),
        ([[[1,3],[4,9],[11,20]], [0,100]], [[0,100]]),
        ([[[10,100],[101,200]], [1,2]], [[1,2],[10,100],[101,200]]),
        ([[[1,5]], [0,3]], [[0,5]]),
        ([[[0,5],[9,12]], [7,16]], [[0,5],[7,16]]),
        ([[[0,3],[6,8],[9,12]], [0,4]], [[0,4],[6,8],[9,12]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.insert(*input)).run(unordered_output=False)
