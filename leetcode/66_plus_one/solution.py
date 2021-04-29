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
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(a) for a in list(str(int(''.join([str(d) for d in digits])) + 1))]


if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ([[1,2,3]], [1,2,4]),
        ([[4,3,2,1]], [4,3,2,2]),
        ([[0]], [1]),
        ([[9,9,9,9,9]], [1,0,0,0,0,0]),
    ]
    Tester.factory(test_cases, func=lambda input: sol.plusOne(*input)).run(unordered_output=False)
