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
    def longestValidParentheses(self, s: str) -> int:
        longest_cnt = 0
        left_cnt, right_cnt = 0, 0
        for char in s:
            if char == '(':
                left_cnt += 1
            elif char == ')':
                if right_cnt + 1 > left_cnt:
                    left_cnt, right_cnt = 0, 0
                else:
                    right_cnt += 1
                    if left_cnt == right_cnt:
                        longest_cnt = max(longest_cnt, left_cnt + right_cnt)
        # print(f'longest: {longest_cnt}')

        left_cnt, right_cnt = 0, 0
        for char in s[::-1]:
            if char == ')':
                left_cnt += 1
            elif char == '(':
                if right_cnt + 1 > left_cnt:
                    left_cnt, right_cnt = 0, 0
                else:
                    right_cnt += 1
                    if left_cnt == right_cnt:
                        longest_cnt = max(longest_cnt, left_cnt + right_cnt)
        # print(f'longest: {longest_cnt}')
        return longest_cnt


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["(()"], 2),
        ([")()())"], 4),
        ([""], 0),
        (["((((((()"], 2),
        (["(((()(((()("], 2),
        (["))()()(())"], 8),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestValidParentheses(*input)).run(unordered_output=False)
