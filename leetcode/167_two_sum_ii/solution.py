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

# input is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2: return []
        left_idx, right_idx = 0, len(numbers) - 1
        while left_idx < right_idx:
            print(f'left: {left_idx}, right: {right_idx}')
            two_sum = numbers[left_idx] + numbers[right_idx]
            if two_sum  == target:
                return [left_idx + 1, right_idx + 1]
            elif two_sum < target:
                left_idx += 1
            else:
                right_idx -= 1
        return []
        
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,7,11,15], 9], [1,2]),
        ([[2,3,4], 6], [1,3]),
        ([[3,3], 6], [1,2]),
        ([[-1,0], -1], [1,2])
    ]

    Tester.factory(test_cases, func=lambda input: sol.twoSum(*input)).run(unordered_output=True)
