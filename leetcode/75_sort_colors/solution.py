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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        left_boundary, right_boundary = 0, len(nums) - 1
        cur = 0
        while cur <= right_boundary:
            # print(nums)
            if nums[cur] == 0:
                tmp = nums[left_boundary]
                nums[left_boundary] = nums[cur]
                nums[cur] = tmp
                left_boundary += 1
                cur += 1
            elif nums[cur] == 2:
                tmp = nums[right_boundary]
                nums[right_boundary] = nums[cur]
                nums[cur] = tmp
                right_boundary -= 1
            else:
                cur += 1
        return nums


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,0,2,1,1,0]], [0,0,1,1,2,2]),
        ([[1,0,2,1,1,0]], [0,0,1,1,1,2]),
        ([[2,0,1]], [0,1,2]),
        ([[0]], [0]),
        ([[1]], [1]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.sortColors(*input)).run(unordered_output=False)
