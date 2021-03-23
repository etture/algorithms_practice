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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in matrix]
        max_square_len = 0
        for r_idx, row in enumerate(matrix):
            for c_idx, elem in enumerate(row):
                if elem == "0":
                    continue
                quadrant_1 = dp[r_idx-1][c_idx] if r_idx-1 >= 0 else 0
                quadrant_2 = dp[r_idx-1][c_idx-1] if r_idx-1 >= 0 and c_idx-1 >= 0 else 0
                quadrant_3 = dp[r_idx][c_idx-1] if c_idx-1 >= 0 else 0
                cur_max_square = min(quadrant_1, quadrant_2, quadrant_3) + 1
                max_square_len = max(max_square_len, cur_max_square)
                dp[r_idx][c_idx] = cur_max_square
        return max_square_len ** 2


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ]
        ], 4),
        ([
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "1", "1", "1"]
            ]
        ], 9),
        ([
            [
                ["1", "0", "1", "1", "1", "0", "0"],
                ["1", "0", "1", "1", "1", "1", "1"],
                ["1", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "1", "1", "1", "1", "1"]
            ]
        ], 9),
        ([
            [
                ["0", "1"],
                ["1", "0"]
            ]
        ], 1),
        ([[["0"]]], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maximalSquare(
        *input)).run(unordered_output=False)
