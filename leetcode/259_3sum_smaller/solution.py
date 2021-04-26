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
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0
        nums_sorted = sorted(nums)
        triplet_set = set()
        triplet_counter = 0
        for pivot in range(len(nums_sorted) - 2):
            # if pivot > 0 and nums_sorted[pivot] == nums_sorted[pivot - 1]:
            #     continue
            # print(f'pivot: {pivot}, nums_sorted[pivot]: {nums_sorted[pivot]}')
            complement = target - nums_sorted[pivot]
            left_idx, right_idx = pivot + 1, len(nums_sorted) - 1
            while left_idx < right_idx:
                two_sum = nums_sorted[left_idx] + nums_sorted[right_idx]
                # print(f'two_sum: {two_sum}')
                if two_sum >= complement:
                    right_idx -= 1
                else:
                    triplet_counter += right_idx - left_idx
                    left_idx += 1
        return triplet_counter
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-2,0,1,3], 2], 2),
        ([[], 0], 0),
        ([[0], 0], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.threeSumSmaller(*input)).run(unordered_output=False)
