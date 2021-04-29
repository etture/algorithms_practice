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
    def splitArray(self, nums: List[int], m: int) -> int:
        if len(nums) < m: return 0
        if m == 0: return 0
        if m == 1: return sum(nums)

        max_num = max(nums)
        sum_all = sum(nums)
        left, right = max_num, sum_all
        global_max = 9999999999
        print(f'max_num: {max_num}')

        while left < right:
            mid = (left + right) // 2
            cur_sum = 0
            cur_iter_max_sum = 0
            cur_group = list()
            all_groups = list()
            for num in nums:
                if cur_sum + num <= mid:
                    cur_sum += num
                    cur_group.append(num)
                else:
                    all_groups.append(cur_group)
                    cur_iter_max_sum = max(cur_iter_max_sum, cur_sum)
                    cur_sum = num
                    cur_group = [num]
            
            all_groups.append(cur_group)
            cur_iter_max_sum = max(cur_iter_max_sum, cur_sum)
            print(f'left: {left}, right: {right}')
            print(f'mid: {mid}, all_groups: {all_groups}, cur_iter_max_sum: {cur_iter_max_sum}, global_max: {min(global_max, cur_iter_max_sum)}')
            if len(all_groups) < m:
                if mid == max_num:
                    return max_num
                if right == mid: break
                right = mid
            elif len(all_groups) > m:
                if left == mid: break
                left = mid
            else:
                global_max = min(global_max, cur_iter_max_sum)
                if right == mid: break
                right = mid
        
        return global_max


test_cases = [
    ([[7,2,5,10,8], 2], 18),
    ([[7,2,5,10,8], 3], 14),
    ([[1,2,3,4,5], 2], 9),
    ([[1,2,3,4,5], 1], 15),
    ([[1,4,4], 3], 4),
    ([[2,3,1,1,1,1,1], 5], 3),
    ([[5,2,1,4,6], 3], 7),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.splitArray(*input)).run(unordered_output=False)
