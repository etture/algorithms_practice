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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        side_len = len(board)
        rows, columns, squares = [list() for _ in range(9)], [list() for _ in range(9)], [[list() for _ in range(3)] for _ in range(3)]
        # print(squares)
        for row in range(side_len):
            square_x = row // 3
            for col in range(side_len):
                element = board[row][col]
                if element.isnumeric():
                    square_y = col // 3
                    if element in rows[row] or element in columns[col] or element in squares[square_x][square_y]: return False
                    rows[row].append(element)
                    columns[col].append(element)
                    squares[square_x][square_y].append(element)
        
        def duplicates_exist(array: List[str]) -> bool:
            return len(array) != len(set(array))
        
        for r in rows:
            # print(f'row: {r}')
            if duplicates_exist(r): return False
        for c in columns:
            # print(f'col: {c}')
            if duplicates_exist(c): return False
        for s_r in squares:
            for s in s_r:
                # print(f'square: {s}')
                if duplicates_exist(s): return False
        return True
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]], True),
        ([[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]], False),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isValidSudoku(*input)).run(unordered_output=False)
