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
    def addBinary(self, a: str, b: str) -> str:
        longer = a if len(a) >= len(b) else b
        shorter = a if len(a) < len(b) else b
        
        answer = list()
        carry = False
        for i in range(len(longer)):
            longer_digit = longer[len(longer)-1-i]
            shorter_digit = shorter[len(shorter)-1-i] if len(shorter) - 1 >= i else "0"
            sum_at_digit = 0
            if carry:
                sum_at_digit += 1
            if longer_digit == "1":
                sum_at_digit += 1
            if shorter_digit == "1":
                sum_at_digit += 1
            
            if sum_at_digit > 1:
                carry = True
            else:
                carry = False

            if sum_at_digit % 2 == 0:
                answer.append("0")
            else:
                answer.append("1")
        
        if carry:
            answer.append("1")

        return "".join(answer[::-1])
            



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["11", "1"], "100"),
        (["1010", "1011"], "10101"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.addBinary(*input)).run(unordered_output=False)
