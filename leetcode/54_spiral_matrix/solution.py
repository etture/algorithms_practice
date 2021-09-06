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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        direction = RIGHT if len(matrix[0]) > 1 else DOWN
        x_min, x_max = 0, len(matrix[0]) - 1
        y_min, y_max = 1, len(matrix) - 1

        answer = list()
        x, y = 0, 0
        while True:
            answer.append(matrix[y][x])
            if direction == RIGHT and x + 1 <= x_max:
                if x + 1 == x_max:
                    direction = DOWN
                    x_max -= 1
                x += 1
            elif direction == DOWN and y + 1 <= y_max:
                if y + 1 == y_max:
                    direction = LEFT
                    y_max -= 1
                y += 1
            elif direction == LEFT and x - 1 >= x_min:
                if x - 1 == x_min:
                    direction = UP
                    x_min += 1
                x -= 1
            elif direction == UP and y - 1 >= y_min:
                if y - 1 == y_min:
                    direction = RIGHT
                    y_min += 1
                y -= 1
            else:
                break
        # print(answer)
        return answer


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[[3],[2]]], [3, 2]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.spiralOrder(
        *input)).run(unordered_output=False)
