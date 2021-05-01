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
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0: return 0

        cumulative_sums = {0: 1}
        cumul_sum = 0
        answer = 0
        for num in nums:
            cumul_sum += num
            if cumul_sum not in cumulative_sums:
                cumulative_sums[cumul_sum] = 0
            diff = cumul_sum - k
            print(f'cumulative_sums: {cumulative_sums}, diff: {diff}')
            if diff in cumulative_sums:
                answer += cumulative_sums[diff]
            cumulative_sums[cumul_sum]+= 1
        return answer




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,1,1], 2], 2),
        ([[1,2,3], 3], 2),
        ([[], 2], 0),
        ([[], 0], 0),
        ([[1,1,1,1,1], 2], 4),
        ([[1,1,1,1,1], 10], 0),
        ([[1], 0], 0),
        ([[-1,-1,1], 0], 1),
        ([[100,1,2,3,4], 6], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.subarraySum(*input)).run(unordered_output=False)
