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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.memo = dict()

        if len(obstacleGrid) == 0: return 0
        if obstacleGrid[0][0] == 1: return 0
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            return 1 if obstacleGrid[0][0] == 0 else 0
        return self.recurse(0, 1) + self.recurse(1, 0)

    def recurse(self, x: int, y: int) -> int:
        coord = (x, y)
        if x >= len(self.grid) or y >= len(self.grid[0]):
            return 0
        if x == len(self.grid) - 1 and y == len(self.grid[0]) - 1:
            return 1 if self.grid[x][y] == 0 else 0
        if coord in self.memo:
            return self.memo[coord]
        if self.grid[x][y] == 1:
            return 0
        self.memo[coord] = self.recurse(x+1, y) + self.recurse(x, y+1)
        return self.memo[coord]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[0,0,0],[0,1,0],[0,0,0]]], 2),
        ([[[0,1],[0,0]]], 1),
        ([[[1]]], 0),
        ([[[0]]], 1),
        ([[[0, 0]]], 1),
        ([[[0, 1]]], 0),
        ([[[1, 0]]], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.uniquePathsWithObstacles(*input)).run(unordered_output=False)
