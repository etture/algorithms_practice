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
    def rob(self, nums: List[int]) -> int:
        answer = [0] * len(nums)
        for idx, num in enumerate(nums):
            if idx == 0 or idx == 1:
                answer[idx] = num
            elif idx == 2:
                answer[idx] = num + answer[idx-2]
            else:
                answer[idx] = num + max(answer[idx-2], answer[idx-3])
        return max(answer)



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3,1]], 4),
        ([[2,7,9,3,1]], 12),
    ]

    Tester.factory(test_cases, func=lambda input: sol.rob(*input)).run(unordered_output=False)
