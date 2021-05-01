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
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        num_units = list()
        while True:
            three_unit = num % 1000
            num_units.append(three_unit)
            num = num // 1000
            if num == 0: break
        print(num_units)

        big_units = ['Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion']
        under_twenty = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                        'Nineteen']
        twenty_ninety = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        answer_str = list()
        for idx, unit in enumerate(num_units):
            cur_str = list()
            _unit = unit

            if unit >= 100:
                hundred_digit = unit // 100
                cur_str.append(under_twenty[hundred_digit-1])
                cur_str.append('Hundred')
                unit -= hundred_digit * 100

            if 0 < unit < 20:
                cur_str.append(under_twenty[unit-1])
            elif 0 < unit:
                ten_digit = unit // 10
                cur_str.append(twenty_ninety[ten_digit-2])
                unit -= ten_digit * 10
                if unit > 0:
                    cur_str.append(under_twenty[unit-1])

            if idx > 0 and _unit > 0:
                cur_str.append(big_units[idx-1])
            if len(cur_str) > 0:
                answer_str.append(cur_str)

        print(answer_str)
        return ' '.join([' '.join(a) for a in answer_str[::-1]]).strip()



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([123], "One Hundred Twenty Three"),
        ([12345], "Twelve Thousand Three Hundred Forty Five"),
        ([1234567], "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
        ([1234567891], "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"),
        ([0], "Zero"),
        ([90], "Ninety"),
        ([711], "Seven Hundred Eleven"),
        ([7011], "Seven Thousand Eleven"),
        ([100], "One Hundred"),
        ([1000], "One Thousand"),
        ([1000000], "One Million"),
        ([50868], "Fifty Thousand Eight Hundred Sixty Eight"),
        ([1000010], "One Million Ten"),
    ]
    Tester.factory(test_cases, func=lambda input: sol.numberToWords(*input)).run(unordered_output=False)
