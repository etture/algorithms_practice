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
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        last_incr_idx = -1
        smallest_bigger_num_idx = -1
        cur_last_incr_num = -1
        for idx, num in enumerate(nums):
            if idx + 1 < len(nums):
                if nums[idx+1] > num:
                    last_incr_idx = idx
                    cur_last_incr_num = num
                    smallest_bigger_num_idx = idx + 1
                else:
                    if nums[idx+1] > cur_last_incr_num:
                        smallest_bigger_num_idx = idx + 1
        
        whole = len(nums)
        if last_incr_idx < 0:
            # flip whole thing
            half = whole // 2
            for i in range(half):
                tmp = nums[i]
                nums[i] = nums[whole-i-1]
                nums[whole-i-1] = tmp
                # print(f'i: {i}')
        else:
            # switch [idx] and idx_ where nums[idx_] is the smallest num bigger than nums[idx]
            # then flip [idx+1:]
            # print(f'last_incr_idx: {last_incr_idx}')
            # print(f'smallest_bigger_idx: {smallest_bigger_num_idx} -> num: {nums[smallest_bigger_num_idx]}')
            tmp = nums[last_incr_idx]
            nums[last_incr_idx] = nums[smallest_bigger_num_idx]
            nums[smallest_bigger_num_idx] = tmp


            whole_remaining = len(nums[last_incr_idx+1:])
            half = whole_remaining // 2
            for i in range(half):
                tmp = nums[last_incr_idx+1+i]
                nums[last_incr_idx+1+i] = nums[whole-i-1]
                nums[whole-i-1] = tmp

        return nums

        

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3]], [1,3,2]),
        ([[3,2,1]], [1,2,3]),
        ([[1,1,5]], [1,5,1]),
        ([[1]], [1]),
        ([[1,2,4,3,7,6,5,9]], [1,2,4,3,7,6,9,5]),
        ([[1,2,4,3,5,6,7,9]], [1,2,4,3,5,6,9,7]),
        ([[1,2,4,3,9,7,6,5]], [1,2,4,5,3,6,7,9]),
        ([[1,2,4,6,9,7,4,3]], [1,2,4,7,3,4,6,9]),
        ([[1,9,9,8,7,6,5,5]], [5,1,5,6,7,8,9,9]),
        ([[2,3,1]], [3,1,2]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.nextPermutation(*input)).run(unordered_output=False)
