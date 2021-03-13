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
    def maxSubArray(self, nums: List[int]) -> int:
        # cur_sum = max_sum = nums[0]
        # for i in range(1, len(nums)):
        #     cur_sum = max(cur_sum + nums[i], nums[i])
        #     max_sum = max(max_sum, cur_sum)
        # return max_sum

        forward, backward = [0] * len(nums), [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                forward[i] = nums[i]
            else:
                forward[i] = max(forward[i-1] + nums[i], nums[i])
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                backward[i] = nums[i]
            else:
                backward[i] = max(backward[i+1] + nums[i], nums[i])
        
        # print(f'forward: {forward}, backward: {backward}')
        final_max = forward[0]
        for i in range(len(nums)):
            final_max = max(final_max, forward[i], backward[i])
        return final_max

    def maxSubArray_naive(self, nums: List[int]) -> int:
        candidates = [0] * len(nums)
        max_num = -9999999999
        tmp_sum = sum(nums)
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1:
                tmp_sum -= nums[i+1]
            candidates[i] = tmp_sum
            max_num = max(max_num, candidates[i])
        # print(candidates)
        # print(f'max: {max_num}')

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                candidates[j] -= nums[i]
                max_num = max(max_num, candidates[j])
        # print(f'max: {max_num}')
        return max_num

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-2,1,-3,4,-1,2,1,-5,4]], 6),
        ([[1]], 1),
        ([[5,4,-1,7,8]], 23),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxSubArray(*input)).run(unordered_output=False)
