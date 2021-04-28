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
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0: return 0
        memo = dict()
        def fewest(total: int) -> int:
            if total in memo: return memo[total]
            candidates = list()
            for coin in coins:
                if total - coin > 0:
                    res = fewest(total-coin)
                    if res != -1:
                        candidates.append(res)
                elif total - coin == 0:
                    candidates.append(0)
            if len(candidates) == 0: 
                memo[total] = -1
            else:
                memo[total] = min(candidates) + 1
            return memo[total]

        return fewest(amount)
    

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,5], 11], 3),
        ([[2], 3], -1),
        ([[1], 0], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.coinChange(*input)).run(unordered_output=False)
