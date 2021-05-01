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

import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set([tuple(x) for x in [p1, p2, p3, p4]])) < 4: return False  # duplicate coordinates
        
        def compare(point: List[int], rest: List[List[int]]):
            slope_set = set()
            distance_set = set()
            for p in rest:
                rise = abs(point[1] - p[1])
                run = abs(point[0] - p[0])
                smaller, larger = min(rise, run), max(rise, run)
                if rise == 0:
                    smaller, larger = rise, run
                abs_slope_repr = smaller / larger
                distance = math.sqrt(rise**2 + run**2)
                slope_set.add(abs_slope_repr)
                distance_set.add(distance)
            return slope_set, distance_set
            
        slope_set_1, distance_set_1 = compare(p1, [p2, p3, p4])
        slope_set_2, distance_set_2 = compare(p2, [p1, p3, p4])
        slope_set_3, distance_set_3 = compare(p3, [p1, p2, p4])
        print(f'slope1: {slope_set_1}, slope2: {slope_set_2}, slope3: {slope_set_3}')
        print(f'dist1: {distance_set_1}, dist2: {distance_set_2}, dist3: {distance_set_3}')
        return slope_set_1 == slope_set_2 == slope_set_3 and distance_set_1 == distance_set_2 == distance_set_3 and \
            len(slope_set_1) == len(slope_set_2) == len(slope_set_3) == 2 and \
                len(distance_set_1) == len(distance_set_2) == len(distance_set_3) == 2
        



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[0,0],[1,1],[1,0],[0,1]], True),
        ([[0,0],[1,1],[1,0],[0,12]], False),
        ([[1,0],[-1,0],[0,1],[0,-1]], True),
        ([[1134,-2539],[492,-1255],[-792,-1897],[-150,-3181]], True),
        ([[1,1],[5,3],[3,5],[7,7]], False),
        ([[1,1],[0,1],[1,2],[0,0]], False),
        ([[0,0],[5,0],[5,4],[0,4]], False),
    ]

    Tester.factory(test_cases, func=lambda input: sol.validSquare(*input)).run(unordered_output=False)
