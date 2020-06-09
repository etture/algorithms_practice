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
logger = Logger(verbose=True)                             
# ----------------------------------------------------------

class Solution:
    def maxProfit_timeout(self, prices: List[int]) -> int:
        max_profit = 0
        for start_idx in range(len(prices)-1):
            for end_idx in range(start_idx+1, len(prices)):
                start_price, end_price = prices[start_idx], prices[end_idx]
                if end_price > start_price:
                    profit = end_price - start_price
                    if profit > max_profit:
                        max_profit = profit
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minmax_vals = list()
        cur_min = 9999999
        for idx in range(len(prices)-1): # getting min
            if prices[idx] < cur_min:
                cur_min = prices[idx]
            minmax_vals.append(cur_min)
        # print(minmax_vals)
        cur_max = 0
        for idx in range(len(prices)-1, 0, -1):
            if prices[idx] > cur_max:
                cur_max = prices[idx]
            minmax_vals[idx-1] = cur_max - minmax_vals[idx-1]
        # print(minmax_vals)
        return max(0, max(minmax_vals))


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([[7,1,5,3,6,4]], 5),
    ([[7,6,4,3,1]], 0),
    ([[]], 0),
    ([[1]], 0),
]

solution = Solution().maxProfit

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
