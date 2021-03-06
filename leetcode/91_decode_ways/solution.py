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
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        total = 1
        cur_one_or_two_length = 0

        for idx, num, in enumerate(s):
            if num == '0':
                if idx - 1 < 0 or s[idx-1] not in ('1','2'):
                    return 0
                elif cur_one_or_two_length-1 > 1:
                    total *= self.fibonacci(cur_one_or_two_length-1)
                cur_one_or_two_length = 0
            elif num == '1':
                cur_one_or_two_length += 1
            elif num == '2':
                cur_one_or_two_length += 1
            elif num in ('7','8','9'):
                if idx - 1 >= 0:
                    if s[idx-1] == '1':
                        total *= self.fibonacci(cur_one_or_two_length+1)
                    elif s[idx-1] == '2':
                        total *= self.fibonacci(cur_one_or_two_length)
                cur_one_or_two_length = 0
            else:
                if idx - 1 >= 0 and s[idx-1] in ('1', '2'):
                    total *= self.fibonacci(cur_one_or_two_length+1)
                cur_one_or_two_length = 0

        if cur_one_or_two_length > 0:
            total *= self.fibonacci(cur_one_or_two_length)
        return total


    def fibonacci(self, num: int) -> int:
        if num == 0: return 0
        memo = {0: 1, 1: 1}
        def internal_recursion(n: int) -> int:
            if n in (0, 1): return memo[n]
            if n-1 not in memo: memo[n-1] = internal_recursion(n-1)
            if n-2 not in memo: memo[n-2] = internal_recursion(n-2)
            return memo[n-1] + memo[n-2]
        return internal_recursion(num)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["12"], 2),
        (["226"], 3),
        (["2226"], 5),
        # 2 2 2 6
        # 2 2 26
        # 22 2 6
        # 22 26
        # 2 22 6

        # 222
        # 2 2 2
        # 22 2
        # 2 22
        (["2261208"], 3),
        (["2271208"], 2),
        (["2221"], 5),
        (["2221208"], 5),
        (["22222"], 8),
        # 2 2 2 2 2
        # 22 2 2 2
        # 2 22 2 2
        # 2 2 22 2
        # 2 2 2 22
        # 22 22 2
        # 22 2 22
        # 2 22 22
        (["222220"], 5),
        (["222229"], 8),
        (["222226"], 13),
        # 2 2 2 2 2 6
        # 2 2 2 2 26
        # 22 2 2 2 6
        # 22 2 2 26
        # 2 22 2 2 6
        # 2 22 2 26
        # 2 2 22 2 6
        # 2 2 22 26
        # 2 2 2 22 6
        # 22 22 2 6
        # 22 22 26
        # 22 2 22
        # 2 22 22
        (["222222"], 13),
        # 2 2 2 2 2 2
        # 22 2 2 2 2
        # 2 22 2 2 2
        # 2 2 22 2 2
        # 2 2 2 22 2
        # 2 2 2 2 22
        # 22 22 2 2
        # 22 2 22 2
        # 22 2 2 22
        # 2 22 22 2
        # 2 22 2 22
        # 2 2 22 22
        # 22 22 22
        (["11106"], 2),
        (["10"], 1),
        (["0"], 0),
        (["06"], 0),
        (["123123"], 9),
        # 1 2 3 1 2 3
        # 12 3 1 2 3
        # 1 23 1 2 3
        # 1 2 3 12 3
        # 1 2 3 1 23
        # 12 3 12 3
        # 12 3 1 23
        # 1 23 12 3
        # 1 23 1 23
        (["2611055971756562"], 4),
    ]
# 1,2,3,5,8,13 -> fibonacci!!
    Tester.factory(test_cases, func=lambda input: sol.numDecodings(*input)).run(unordered_output=False)
