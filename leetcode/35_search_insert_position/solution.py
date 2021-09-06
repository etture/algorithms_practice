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
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            middle = (left + right) // 2
            # print(f'left: {left}, right: {right}, middle: {middle}')
            if nums[middle] == target:
                return middle
            elif left >= right:
                if nums[left] < target:
                    return left + 1
                else:
                    return left
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,3,5,6], 5], 2),
        ([[1,3,5,6], 2], 1),
        ([[1,3,5,6], 7], 4),
        ([[1,3,5,6], 0], 0),
        ([[1], 0], 0),
        ([[1,3], 0], 0),
        ([[3,5,7,9,10], 8], 3),
    ]

    Tester.factory(test_cases, func=lambda input: sol.searchInsert(*input)).run(unordered_output=False)
