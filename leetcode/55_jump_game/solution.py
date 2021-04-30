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
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        position = len(nums) - 2
        target = len(nums) - 1
        closest_jumpable = -1
        while position >= 0:
            if position + nums[position] >= target:
                target = position
                closest_jumpable = position
            position -= 1
        return closest_jumpable == 0

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,3,1,1,4]], True),
        ([[3,2,1,0,4]], False),
        ([[5,2,1,0,4]], True),
        ([[3,5,1,0,4]], True),
    ]

    Tester.factory(test_cases, func=lambda input: sol.canJump(*input)).run(unordered_output=False)
