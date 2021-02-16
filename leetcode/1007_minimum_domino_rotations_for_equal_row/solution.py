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

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        length = len(A)

        # Count if there are enough of the same number to fill a row
        num_dict = dict()
        for num in range(1, 7):
            num_dict[num] = 0
        for i in range(length):
            pair = set([A[i], B[i]])
            for p in pair:
                num_dict[p] += 1
        
        # print(num_dict)

        for num, count in num_dict.items():
            if count == length:
                a_count, b_count = 0, 0
                for i in range(length):
                    if A[i] != B[i]:
                        if A[i] == num:
                            a_count += 1
                        if B[i] == num:
                            b_count += 1
                return a_count if a_count < b_count else b_count
                
        return -1


test_cases = [
    ([[2,1,2,4,2,2], [5,2,6,2,3,2]], 2),
    ([[3,5,1,2,3], [3,6,3,3,4]], -1),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.minDominoRotations(*input)).run(unordered_output=False)
