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
    def countSmaller_naive(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] < nums[j]:
                    ans[j] += 1
        return ans

    def countSmaller(self, nums: List[int]) -> List[int]:  # kinda use merge sort
        count_to_right_smaller = [0] * len(nums)
        def merge_count(start: int, end: int) -> List[Tuple[int, int]]:  # (val, idx)
            # print(f'start: {start}, end: {end}')
            if start >= end:
                return [(nums[start], start)]
            middle = (start+end) // 2
            left = merge_count(start, middle)
            right = merge_count(middle+1, end)

            merged = list()
            while len(left) > 0 or len(right) > 0:
                # print(f'  left: {left}, right: {right}')
                if len(left) == 0:
                    merged.append(right.pop(0))
                elif len(right) == 0:
                    # print(f'inside len(right)==0, left: {left}, right: {right}')
                    merged.append(left.pop(0))

                elif right[0][0] >= left[0][0]:
                    merged.append(right.pop(0))
                else:
                    merged.append(left.pop(0))
                    count_to_right_smaller[merged[-1][1]] += len(right)

            # print(f'{start}, {end} -> count_to_right: {count_to_right_smaller}')
            return merged
        after_sort = merge_count(0, len(nums)-1)
        return count_to_right_smaller
            



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[5,2,6,1]], [2,1,1,0]),
        ([[-1]], [0]),
        ([[-1,-1]], [0,0]),
        ([[10,9,8,7,6,5,4,3,2,1]], [9,8,7,6,5,4,3,2,1,0]),
        ([[1,2,3,4,5]], [0,0,0,0,0]),
        ([[5,3,1,2,4]], [4,2,0,0,0]),
        ([[3,1,1,1,1]], [4,0,0,0,0]),
        ([[10, 8, 2, 4, 6, 1, 9]], [6,4,1,1,1,0,0]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.countSmaller(*input)).run(unordered_output=False)
