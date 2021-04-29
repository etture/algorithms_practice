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
    def consecutiveNumbersSum(self, N: int) -> int:
        # sliding window
        if N < 1: return 0
        start = 1
        end = 2
        stop_point = N // 2
        sum_val = start + end
        answer = 1
        while start <= stop_point:
            if sum_val == N:
                answer += 1
                sum_val -= start
                sum_val += end + 1
                start += 1
                end += 1
            elif sum_val < N:
                sum_val += end + 1
                end += 1
            elif sum_val > N:
                sum_val -= start
                start += 1
            # print(f'answer: {answer}, sum_val: {sum_val}, start: {start}, end: {end}')
                
        return answer

                

            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([5], 2),
        ([9], 3),
        ([15], 4),
        ([14], 2),
    ]

    Tester.factory(test_cases, func=lambda input: sol.consecutiveNumbersSum(*input)).run(unordered_output=False)
