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
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        results = list()
        for idx_1, n1 in enumerate(reversed(num1)):
            carry = 0
            cur_result = [0] * idx_1
            for idx_2, n2 in enumerate(reversed(num2)):
                prod = (int(n1) * int(n2)) + carry
                carry = (prod - (prod % 10)) // 10
                cur_result.append(prod % 10)
                # print(f'n1: {n1}, n2: {n2}, prod: {prod}, carry: {carry}, res: {prod%10}')
            cur_result.append(carry)
            results.append(cur_result)
        longest = max([len(a) for a in results])
        carry = 0
        total = list()
        for i in range(longest):
            cur_sum = carry
            for res in results:
                if i < len(res):
                    cur_sum += res[i]
            if cur_sum >= 10:
                carry = (cur_sum - (cur_sum % 10)) // 10
            else:
                carry = 0
            total.append(cur_sum % 10)
        total.append(carry)
        print(results)
        print(f'total: {list(reversed(total))}')
        start_point = 0
        for idx, num in enumerate(total[::-1]):
            print(f'idx: {idx}, num: {num}')
            if num > 0:
                start_point = idx
                break
        print(f'start_point: {start_point}')
        print([str(a) for a in total[::-1][start_point:]])
        return ''.join([str(a) for a in total[::-1][start_point:]])




if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        (["2", "3"], "6"),
        (["123", "456"], "56088"),
    ]
    Tester.factory(test_cases, func=lambda input: sol.multiply(*input)).run(unordered_output=False)
