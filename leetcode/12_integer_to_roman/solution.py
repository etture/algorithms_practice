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
    def intToRoman(self, num: int) -> str:
        convert_map = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }

        digit_list = list()
        multiplier = 1
        
        while num > 0:
            digit = num % 10
            num_str = ''
            if 1 <= digit <= 3:
                num_str = convert_map[1 * multiplier] * digit
            elif digit == 4:
                num_str = convert_map[1 * multiplier] + convert_map[5 * multiplier]
            elif digit == 5:
                num_str = convert_map[5 * multiplier]
            elif 6 <= digit <= 8:
                num_str = convert_map[5 * multiplier] + convert_map[1 * multiplier] * (digit - 5)
            elif digit == 9:
                num_str = convert_map[1 * multiplier] + convert_map[10 * multiplier]
            digit_list.append(num_str)            
            
            num = num // 10
            multiplier *= 10
        
        return ''.join(digit_list[::-1])
            


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([3], 'III'),
        ([4], 'IV'),
        ([9], 'IX'),
        ([58], 'LVIII'),
        ([1994], 'MCMXCIV'),
    ]

    Tester.factory(test_cases, func=lambda input: sol.intToRoman(*input)).run(unordered_output=False)
