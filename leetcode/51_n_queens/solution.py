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
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.answer = list()
        self.recurse(prev_pos=list(), row_idx=0)
        return self.answer

    def recurse(self, prev_pos: List[tuple[int]], row_idx: int):
        cols_to_avoid = set()

        if row_idx > 0:
            # all used columns
            cols_to_avoid.update([x[1] for x in prev_pos])

            # adjacent columns to previous row
            if prev_pos[-1][1] - 1 >= 0:
                cols_to_avoid.add(prev_pos[-1][1] - 1)
            if prev_pos[-1][1] + 1 < self.n:
                cols_to_avoid.add(prev_pos[-1][1] + 1)

            # all diagonals
            for pos in prev_pos:
                for col_idx in range(self.n):
                    if abs(pos[0] - row_idx) == abs(pos[1] - col_idx):
                        cols_to_avoid.add(col_idx)

        for col_idx in range(self.n):
            if col_idx in cols_to_avoid: continue
            tmp_combination = prev_pos + [tuple([row_idx, col_idx])]
            if len(tmp_combination) == self.n:
                one_answer = list()
                for x in tmp_combination:
                    one_answer.append("".join(['Q' if i == x[1] else '.' for i in range(self.n)]))
                self.answer.append(one_answer)
            else:
                self.recurse(tmp_combination, row_idx + 1)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([4], [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        ([1], [["Q"]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solveNQueens(*input)).run(unordered_output=True)
