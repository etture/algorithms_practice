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
    def combine(self, n: int, k: int) -> List[List[int]]:
        answers = list()
        for num in range(1, n+2-k):
            # print(f'num: {num}')
            answers.extend(self.recurse(num, n, k))
        return answers

    def recurse(self, start: int, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[start]]
        if k <= 0:
            return []
        answers = list()
        for num in range(start+1, n+3-k):  # (n+3-k) == (n+2-(k-1)) 
            answers.extend(self.recurse(num, n, k-1))
        # print(f'start: {start}, n: {n}, k: {k}, answers: {answers}')
        # print(f'  returned: {[[start, *x] for x in answers]}')
        return [[start, *x] for x in answers]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([4,2], [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]),
        ([1,1], [[1]]),
        ([2,2], [[1,2]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.combine(*input)).run(unordered_output=True)
