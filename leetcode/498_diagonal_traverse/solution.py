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
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = list()
        x, y = 0, 0
        NORTHEAST, SOUTHWEST = (1, -1), (-1, 1)
        direction = NORTHEAST
        while True:
            # print(f'direction: {direction}, coord: ({x}, {y})')
            direction_change = True
            answer.append(mat[y][x])
            x += direction[0]
            y += direction[1]
            if x < 0:
                if y >= len(mat):  # bottom left corner
                    x += 2
                    y -= 1
                else:
                    x += 1
            elif x >= len(mat[0]):
                # same case if top right corner
                x -= 1
                y += 2
            elif y < 0:
                y += 1
            elif y >= len(mat):
                x += 2
                y -= 1
            else:
                direction_change = False

            # print(f'direction change? {direction_change}, changed_coord: ({x}, {y})')
            if direction_change:
                if direction == NORTHEAST: direction = SOUTHWEST
                else: direction = NORTHEAST

            if x < 0 or x >= len(mat[0]) or y < 0 or y >= len(mat):
                break
        return answer




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,2,3],[4,5,6],[7,8,9]]], [1,2,4,7,5,3,6,8,9]),
        ([[[1,2],[3,4]]], [1,2,3,4]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.findDiagonalOrder(*input)).run(unordered_output=False)
