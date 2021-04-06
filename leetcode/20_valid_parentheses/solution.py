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
    def isValid(self, s: str) -> bool:
        stack = list()
        match = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            elif char in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                elif stack[-1] == match[char]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0

            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["()"], True),
        (["()[]{}"], True),
        (["(]"], False),
        (["([)]"], False),
        (["{[]}"], True),
        (["()"], True),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isValid(*input)).run(unordered_output=False)
