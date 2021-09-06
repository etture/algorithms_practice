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
    def generateParenthesis(self, n: int) -> List[str]:
        def recurse(cur_combo: List[str]):
            nonlocal left_bucket, right_bucket

            if left_bucket == 0 and right_bucket == 0:
                answers.append("".join(cur_combo))

            if left_bucket > 0:
                left_bucket -= 1
                recurse(cur_combo + ["("])
                left_bucket += 1
            if right_bucket - 1 >= left_bucket:
                right_bucket -= 1
                recurse(cur_combo + [")"])
                right_bucket += 1

        answers = list()
        left_bucket, right_bucket = n, n
        left_used, right_used = list(), list()
        recurse(list())
        return answers
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([3], ["((()))","(()())","(())()","()(())","()()()"]),
        ([1], ["()"]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.generateParenthesis(*input)).run(unordered_output=True)
