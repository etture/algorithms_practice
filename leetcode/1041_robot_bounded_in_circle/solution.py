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
    def isRobotBounded(self, instructions: str) -> bool:
        directions = ['north', 'east', 'south', 'west']
        direction = 0
        coord = [0, 0]

        dir_map = {
            'north': (1, 1),
            'south': (1, -1),
            'east': (0, 1),
            'west': (0, -1),
        }

        # My Solution -- it was good too
        # for _ in range(4):
            # for inst in instructions:
            #     if inst == 'G':
            #         coord[dir_map[directions[direction]][0]] += dir_map[directions[direction]][1]
            #     elif inst == 'L':
            #         direction = (direction - 1) % 4
            #     elif inst == 'R':
            #         direction = (direction + 1) % 4
            #     print(f'dir: {directions[direction]}, coord: {coord}')
        
        # if coord == [0, 0]: return True
        # else: return False

        for inst in instructions:
            if inst == 'G':
                coord[dir_map[directions[direction]][0]] += dir_map[directions[direction]][1]
            elif inst == 'L':
                direction = (direction - 1) % 4
            elif inst == 'R':
                direction = (direction + 1) % 4
            print(f'dir: {directions[direction]}, coord: {coord}')
        
        return coord == [0, 0] or direction != 0


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["GGLLGG"], True),
        (["GG"], False),
        (["GL"], True),
        (["LLLG"], True),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isRobotBounded(*input)).run(unordered_output=False)
