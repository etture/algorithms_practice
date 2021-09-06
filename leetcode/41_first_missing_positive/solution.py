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
    def firstMissingPositive(self, nums: List[int]) -> int:
        # with hashmap
        hashmap = dict()
        for i in range(1, len(nums)+2):
            hashmap[i] = 0
        for num in nums:
            if num <= 0 or num > len(nums)+1:
                continue
            hashmap[num] += 1
        min_num = 999999
        for k, v in hashmap.items():
            if v == 0:
                min_num = min(min_num, k)
        return min_num
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,0]], 3),
        ([[5,1]], 2),
        ([[3,4,-1,1]], 2),
        ([[1,-1,4,3]], 2),
        ([[7,8,9,11,12]], 1),
        ([[12,11,9,8,7]], 1),
        ([[14,12,11,13,9,8,7]], 1),
        ([[12,11,9,8,7,6,5,4,3,2,1]], 10),
        ([[12,11,9,8,7,6,5,3,2,1]], 4),
        ([[]], 1),
        ([[3,2,1,5]], 4),
        ([[3,1]], 2),
        ([[4,1,2]], 3),
        ([[2,1,4]], 3),
        ([[1,2,3,4,5,7,8,800]], 6),
    ]

    Tester.factory(test_cases, func=lambda input: sol.firstMissingPositive(*input)).run(unordered_output=False)
