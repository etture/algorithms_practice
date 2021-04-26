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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = dict()
        for idx, num in enumerate(nums):
            indexes[num] = idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in indexes and indexes[complement] != idx:
                return [idx, indexes[complement]]
        
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,7,11,15], 9], [0,1]),
        ([[3,2,4], 6], [1,2]),
        ([[3,3], 6], [0,1])
    ]

    Tester.factory(test_cases, func=lambda input: sol.twoSum(*input)).run(unordered_output=True)
