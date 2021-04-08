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
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        sorted_nums = sorted(nums)
        counter = 0
        max_consecutive = 0
        last = None
        for n in sorted_nums:
            if counter == 0:
                counter += 1
            elif n == last:
                continue
            elif n == last + 1:
                counter += 1
            else:
                counter = 1
            # print(f'n: {n}, counter: {counter}')
            last = n
            max_consecutive = max(max_consecutive, counter)
        return max_consecutive
                
                

            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[100,4,200,1,3,2]], 4),
        ([[0,3,7,2,5,8,4,6,0,1]], 9),
        ([[]], 0),
        ([[1]], 1),
        ([[1,5,3,7,9,12]], 1),
        ([[1,2,0,1]], 3),
        ([[1,2,0,1,1,1,1,1,1,1,1,1,0,1,1,1,2,2,2,2,2,2]], 3),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestConsecutive(*input)).run(unordered_output=False)
