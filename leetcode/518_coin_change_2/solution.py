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
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in sorted(coins):
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([4, [1,2]], 3),
        ([5,[1,2,5]], 4),
        ([10,[1,2,5]], 10),
        ([3,[2]], 0),
        ([10,[10]], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.change(*input)).run(unordered_output=False)
