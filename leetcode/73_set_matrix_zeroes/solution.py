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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_set, c_set = set(), set()
        for r_idx, row in enumerate(matrix):
            for c_idx, elem in enumerate(row):
                if elem == 0:
                    r_set.add(r_idx)
                    c_set.add(c_idx)
        
        for r in r_set:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        for c in c_set:
            for i in range(len(matrix)):
                matrix[i][c] = 0

        return matrix


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[1,1,1],[1,0,1],[1,1,1]]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[[0,1,2,0],[3,4,5,2],[1,3,1,5]]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.setZeroes(*input)).run(unordered_output=False)
