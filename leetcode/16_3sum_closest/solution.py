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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sorted = sorted(nums)
        MAX_NUM = 99999999
        global_smallest_diff = MAX_NUM
        global_closest_sum = MAX_NUM
        print(f'nums_sorted: {nums_sorted}')
        for pivot in range(len(nums) - 2):
            complement = target - nums_sorted[pivot]
            left_idx, right_idx = pivot + 1, len(nums_sorted) - 1
            cur_smallest_diff = MAX_NUM
            cur_closest_sum = MAX_NUM
            print(f'pivot: {pivot}, nums_sorted[pivot]: {nums_sorted[pivot]}, target_complement: {complement}')
            while left_idx < right_idx:
                two_sum = nums_sorted[left_idx] + nums_sorted[right_idx]
                diff = abs(complement - two_sum)
                print(f'   left: {left_idx} -> {nums_sorted[left_idx]}, right: {right_idx} -> {nums_sorted[right_idx]}, two_sum: {two_sum}, diff: {diff}')
                if diff < cur_smallest_diff:
                    cur_smallest_diff = diff
                    cur_closest_sum = nums_sorted[pivot] + two_sum
                if two_sum == complement:
                    break
                elif two_sum < complement:
                    left_idx += 1
                else:
                    right_idx -= 1
            if cur_smallest_diff < global_smallest_diff:
                global_smallest_diff = cur_smallest_diff
                global_closest_sum = cur_closest_sum
                if global_closest_sum == target:
                    break
        return global_closest_sum

            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-1,2,1,-4], 1], 2),
        ([[-1,2,1,-4,4,1], 1], 1),
        ([[0,2,1,-3], 1], 0),
        ([[4,0,5,-5,3,3,0,-4,-5], -2], -2),
        ([[-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.threeSumClosest(*input)).run(unordered_output=False)
