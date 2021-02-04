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
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        cur_idx = 0
        look_ahead_idx = 1

        unique_cnt = 1

        highest_observed_val = nums[cur_idx]

        while look_ahead_idx < len(nums):
            if nums[look_ahead_idx] > highest_observed_val:
                highest_observed_val = nums[look_ahead_idx]
                cur_idx += 1
                # tmp = nums[look_ahead_idx]
                # nums[look_ahead_idx] = nums[cur_idx]
                # nums[cur_idx] = tmp
                nums[cur_idx] = nums[look_ahead_idx]
            look_ahead_idx += 1

        print(nums)

        return cur_idx + 1


test_cases = [
    ([[1,1,2]], 2),
    ([[0,0,1,1,1,2,2,3,3,4]], 5),
]

if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.removeDuplicates(*input)).run(unordered_output=False)
