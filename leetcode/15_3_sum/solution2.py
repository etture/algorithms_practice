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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums_sorted = sorted(nums)
        answer = set()
        for pivot in range(len(nums_sorted) - 2):
            if pivot > 0 and nums_sorted[pivot] == nums_sorted[pivot - 1]:
                continue
            complement = -nums_sorted[pivot]
            left_idx = pivot + 1
            right_idx = len(nums_sorted) - 1
            while left_idx < right_idx:
                two_sum = nums_sorted[left_idx] + nums_sorted[right_idx]
                if two_sum == complement:
                    answer.add((nums_sorted[pivot], nums_sorted[left_idx], nums_sorted[right_idx]))
                    left_idx += 1
                    right_idx -= 1
                elif two_sum < complement:
                    left_idx += 1
                else:
                    right_idx -= 1
        # print(answer)
        return [list(a) for a in list(answer)]
                
                    
        
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-1,0,1,2,-1,-4]], [[-1,-1,2],[-1,0,1]]),
        ([[]], []),
        ([[0]], []),
    ]

    Tester.factory(test_cases, func=lambda input: sol.threeSum(*input)).run(unordered_output=True)
