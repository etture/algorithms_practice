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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        
        self.matrix = matrix
        self.memo = dict()  # key: tuple([row, col])
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

        max_len = 0

        for r_idx, row in enumerate(matrix):
            for c_idx, elem in enumerate(row):
                increasing_path_length = self.check_increasing_path(r_idx, c_idx)
                max_len = max(max_len, increasing_path_length)

        return max_len

    def check_increasing_path(self, r_idx: int, c_idx: int) -> int:
        # print(f'coords -> r_idx: {r_idx}, c_idx: {c_idx}')
        coordinates_key = tuple([r_idx, c_idx])
        if coordinates_key in self.memo:
            # print(f'  memo found -> {self.memo[coordinates_key]}')
            return self.memo[coordinates_key]

        cur_val = self.matrix[r_idx][c_idx]
        up, down, left, right = 1, 1, 1, 1

        if r_idx-1 >= 0 and self.matrix[r_idx-1][c_idx] > cur_val:  # look up
            up += self.check_increasing_path(r_idx-1, c_idx)
        if r_idx+1 < self.num_rows and self.matrix[r_idx+1][c_idx] > cur_val:  # look down
            down += self.check_increasing_path(r_idx+1, c_idx)
        if c_idx-1 >= 0 and self.matrix[r_idx][c_idx-1] > cur_val:  # look left
            left += self.check_increasing_path(r_idx, c_idx-1)
        if c_idx+1 < self.num_cols and self.matrix[r_idx][c_idx+1] > cur_val:  # look right
            right += self.check_increasing_path(r_idx, c_idx+1)

        self.memo[coordinates_key] = max(up, down, left, right)
        # print(f'  memo set: {self.memo[coordinates_key]}')
        return self.memo[coordinates_key]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                [
                    [9,9,4],
                    [6,6,8],
                    [2,1,1]
                ]
            ], 
        4),
        (
            [
                [
                    [3,4,5],
                    [3,2,6],
                    [2,2,1]
                ]
            ],
        4),
        (
            [[[1]]],
            1
        ),
        (
            [[]], 0
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestIncreasingPath(*input)).run(unordered_output=False)
