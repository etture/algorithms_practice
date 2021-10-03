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
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        cur_dir = 0

        def next_dir():
            nonlocal cur_dir
            cur_dir = (cur_dir + 1) % 4

        filled = 0
        row, col = 0, 0
        while filled <= n ** 2:
            filled += 1
            matrix[row][col] = filled
            # first try
            if not (0 <= row + dirs[cur_dir][0] < n and 0 <= col + dirs[cur_dir][1] < n) or \
                    matrix[row + dirs[cur_dir][0]][col + dirs[cur_dir][1]] != 0:
                next_dir()
            
            # second try
            if not (0 <= row + dirs[cur_dir][0] < n and 0 <= col + dirs[cur_dir][1] < n) or \
                    matrix[row + dirs[cur_dir][0]][col + dirs[cur_dir][1]] != 0:
                break
            
            row += dirs[cur_dir][0]
            col += dirs[cur_dir][1]
        # print(matrix)
        return matrix


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([4], [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]),
        ([3], [[1,2,3],[8,9,4],[7,6,5]]),
        ([2], [[1,2],[4,3]]),
        ([1], [[1]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.generateMatrix(*input)).run(unordered_output=False)
