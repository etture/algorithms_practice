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
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.memo = dict()
        _m, _n = 0, 0
        return self.traverse_dp(_m, _n)

    def traverse_dp(self, _m: int, _n: int) -> int:
        coord = (_m, _n)
        if coord in self.memo:
            return self.memo[coord]
        if _m >= self.m or _n >= self.n: return 0
        if _m == self.m - 1 and _n == self.n - 1:
            self.memo[coord] = 1
            return 1
        self.memo[coord] = self.traverse_dp(_m+1, _n) + self.traverse_dp(_m, _n+1)
        return self.memo[coord]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([3, 7], 28),
        ([3, 2], 3),
        ([7, 3], 28),
        ([3, 3], 6),
    ]

    Tester.factory(test_cases, func=lambda input: sol.uniquePaths(*input)).run(unordered_output=False)
