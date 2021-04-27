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
        if len(matrix) < 1: return 0
        memo_matrix = list()
        for _ in range(len(matrix)):
            row = list()
            for _ in range(len(matrix[0])):
                row.append(0)
            memo_matrix.append(row)
        max_path = 0

        def longest_path(r: int, c: int) -> int:
            if memo_matrix[r][c] > 0:
                print(f'r: {r}, c: {c}, memo_matrix: {memo_matrix}, exit condition')
                return memo_matrix[r][c]

            directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
            cur_max = 0
            for d in directions:
                new_r, new_c = r + d[0], c + d[1]
                if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
                    if matrix[new_r][new_c] <= matrix[r][c]:
                        continue
                    elif memo_matrix[new_r][new_c] == 0:
                        cur_max = max(cur_max, longest_path(new_r, new_c))
                    else:
                        cur_max = max(cur_max, memo_matrix[new_r][new_c])
            memo_matrix[r][c] = cur_max + 1
            print(f'r: {r}, c: {c}, memo_matrix: {memo_matrix}, loop')
            return memo_matrix[r][c]


        for r_idx in range(len(matrix)):
            for c_idx in range(len(matrix[0])):
                max_path = max(max_path, longest_path(r_idx, c_idx))
        # print(f'memo_matrix: {memo_matrix}')
        return max_path


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
