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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        processed = sorted(nums)
        # print(processed)
        return processed[-k]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[3,2,1,5,6,4], 2], 5),
        ([[3,2,3,1,2,4,5,5,6], 4], 4),
    ]

    Tester.factory(test_cases, func=lambda input: sol.findKthLargest(*input)).run(unordered_output=False)
