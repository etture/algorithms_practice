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
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.memo = dict()

        return self.recurse(0, 0)
    
    def recurse(self, x: int, y: int) -> int:
        if x >= self.m or y >= self.n:
            return -1
        if x == self.m - 1 and y == self.n - 1:
            return self.grid[x][y]
        if (x, y) in self.memo:
            return self.memo[(x, y)]
        min_path = self.grid[x][y] + min([a for a in [self.recurse(x+1, y), self.recurse(x, y+1)] if a >= 0])
        self.memo[(x,y)] = min_path
        return min_path


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,3,1],[1,5,1],[4,2,1]]], 7),
        ([[[1,2,3],[4,5,6]]], 12),
        ([[[0,0],[0,0]]], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minPathSum(*input)).run(unordered_output=False)
