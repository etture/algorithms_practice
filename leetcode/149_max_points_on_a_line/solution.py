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
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 0:
            return 0
        if len(points) == 1:
            return 1

        function_map = dict()  # key: (slope, y-intercept), val: {'sum': int, 'coords': List[tuple(x, y)]}

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                point_a = points[i]
                point_b = points[j]


                if (point_b[0] - point_a[0]) == 0:
                    key = tuple([None, point_b[0]])
                else:
                    slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
                    y_int = point_b[1] - (slope * point_b[0])
                    key = tuple([slope, y_int])

                # print(f'point_a: {point_a}, point_b: {point_b} => key: {key}')
                if key not in function_map:
                    function_map[key] = {
                        'sum': 2,
                        'coords': set([tuple(point_a), tuple(point_b)])
                    }
                else: 
                    if tuple(point_a) not in function_map[key]['coords']:
                        function_map[key]['coords'].add(tuple(point_a))
                        function_map[key]['sum'] += 1
                    if tuple(point_b) not in function_map[key]['coords']:
                        function_map[key]['coords'].add(tuple(point_b))
                        function_map[key]['sum'] += 1
                    
        
        # print(function_map)

        return max([x['sum'] for x in function_map.values()])



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,1],[2,2],[3,3]]], 3),
        ([[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]], 4),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxPoints(*input)).run(unordered_output=False)
