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
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = list()
        self.run(list(), nums)
        return self.answer

    def run(self, head: List[int], tail: List[int]):
        if len(tail) == 0:
            self.answer.append(head)
        else:
            for idx in range(len(tail)):
                self.run(head+[tail[idx]], tail[:idx] + tail[idx+1:])




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[1,2,3]], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([[0,1]], [[0,1],[1,0]]),
        ([[1]], [[1]]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.permute(*input)).run(unordered_output=True)
