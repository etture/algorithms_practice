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
import pprint
pp = pprint.PrettyPrinter()

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) < 1:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        prev_rows_cumulative = dict()
        max_rect_area = 0

        for row_idx in range(num_rows):
            prev_rows_cumulative[row_idx] = dict()
            contiguous = 0
            for col_idx in range(num_cols):
                if matrix[row_idx][col_idx] == "1":
                    contiguous += 1
                    end_idx = col_idx
                    for start_idx in range(col_idx - (contiguous - 1), col_idx + 1):
                        range_idx = (start_idx, end_idx)
                        range_sum = end_idx - start_idx + 1
                        # print(f'    range: {range_idx}, range_sum: {range_sum}')
                        if row_idx > 0 and range_idx in prev_rows_cumulative[row_idx-1]:
                            prev_rows_cumulative[row_idx][range_idx] = range_sum + prev_rows_cumulative[row_idx-1][range_idx]
                        else:
                            prev_rows_cumulative[row_idx][range_idx] = range_sum
                        max_rect_area = max(max_rect_area, prev_rows_cumulative[row_idx][range_idx])
                elif matrix[row_idx][col_idx] == "0":
                    contiguous = 0
                # print(f'row: {row_idx}, col: {col_idx}, contig: {contiguous}, prev: {prev_rows_cumulative}')

        # pp.pprint(prev_rows_cumulative)
        return max_rect_area


    def maximalRectangle_inefficient(self, matrix: List[List[str]]) -> int:
        if len(matrix) < 1:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        prev_rows_cumulative = dict()
        max_rect_area = 0

        for row_idx in range(num_rows):
            prev_rows_cumulative[row_idx] = dict()
            for col_idx in range(num_cols):
                if matrix[row_idx][col_idx] == "1":
                    contiguous = list()
                    for tmp_idx in range(col_idx, num_cols):
                        if matrix[row_idx][tmp_idx] == "1":
                            contiguous.append(matrix[row_idx][tmp_idx])
                            start_idx = tmp_idx - (len(contiguous) - 1)
                            end_idx = tmp_idx
                            range_idx = (start_idx, end_idx)
                            if row_idx > 0 and range_idx in prev_rows_cumulative[row_idx-1]:
                                prev_rows_cumulative[row_idx][range_idx] = len(contiguous) + prev_rows_cumulative[row_idx-1][range_idx]
                            else:
                                prev_rows_cumulative[row_idx][range_idx] = len(contiguous)
                            max_rect_area = max(max_rect_area, prev_rows_cumulative[row_idx][range_idx])
                        elif matrix[row_idx][tmp_idx] == "0":
                            contiguous = list()             
        # print(prev_rows_cumulative)
        return max_rect_area


    def maximalRectangle_inefficient_with_contiguous_as_number_instead_of_list(self, matrix: List[List[str]]) -> int:
        if len(matrix) < 1:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        prev_rows_cumulative = dict()
        max_rect_area = 0

        for row_idx in range(num_rows):
            prev_rows_cumulative[row_idx] = dict()
            for col_idx in range(num_cols):
                if matrix[row_idx][col_idx] == "1":
                    contiguous = 0
                    for tmp_idx in range(col_idx, num_cols):
                        if matrix[row_idx][tmp_idx] == "1":
                            contiguous += 1
                            start_idx = tmp_idx - (contiguous - 1)
                            end_idx = tmp_idx
                            range_idx = (start_idx, end_idx)
                            if row_idx > 0 and range_idx in prev_rows_cumulative[row_idx-1]:
                                prev_rows_cumulative[row_idx][range_idx] = contiguous + prev_rows_cumulative[row_idx-1][range_idx]
                            else:
                                prev_rows_cumulative[row_idx][range_idx] = contiguous
                            max_rect_area = max(max_rect_area, prev_rows_cumulative[row_idx][range_idx])
                        elif matrix[row_idx][tmp_idx] == "0":
                            contiguous = 0
        # print(prev_rows_cumulative)
        return max_rect_area


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[ ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]]], 
            6),
        ([[]], 0),
        ([[["0"]]], 0),
        ([[["1"]]], 1),
        ([[["0","0"]]], 0),
        ([[["0","0","0","0","0"],["0","1","1","1","0"],["0","1","1","1","0"],["0","1","1","1","0"],["0","0","0","0","0"]]], 9),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maximalRectangle(*input)).run(unordered_output=False)
