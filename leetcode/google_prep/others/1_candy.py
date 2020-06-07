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
    def candy_timeout(self, ratings: List[int]) -> int:
        candy_line = [0] * len(ratings)
        for idx, child in enumerate(ratings):
            candy_line[idx] += 1
            if idx > 0:
                if child > ratings[idx - 1]:
                    candy_line[idx] += candy_line[idx - 1]
                elif child < ratings[idx - 1] \
                        and candy_line[idx - 1] <= candy_line[idx]:
                    working_idx = idx
                    while working_idx > 0 \
                            and ratings[working_idx] < ratings[working_idx - 1] \
                            and candy_line[working_idx - 1] <= candy_line[working_idx]:
                        candy_line[working_idx - 1] += 1
                        working_idx -= 1
        # print(candy_line)
        return sum(candy_line)

    def candy_bad_attempt(self, ratings: List[int]) -> int:
        def add_decr(num: int) -> int:
            mult_factor = num // 2
            if num % 2 == 0:
                return (num+1) * mult_factor
            else:
                return ((num+1) * mult_factor) + (mult_factor+1)

        candy_line = [0] * len(ratings)
        decr_start = None
        incr_start = None
        incr_value = 0
        total_candies = 0
        for idx in range(len(ratings)):
            if idx == 0:
                incr_value = 1
                total_candies += incr_value
            
            else:
                if ratings[idx] < ratings[idx-1]:
                    if decr_start is None:
                        decr_start = idx - 1
                        incr_start = None
                    
                else:
                    if decr_start:
                        decr_len = (idx - 1) - decr_start
                        if incr_value >= decr_len:
                            total_candies += add_decr(decr_len-1)
                            total_candies += incr_value
                        else:
                            total_candies += add_decr(decr_len-1)
                            total_candies -= decr_len - incr_value
                    decr_start = None
                    if ratings[idx] == ratings[idx-1]:
                        incr_value = 1
                        total_candies += incr_value
                    else:  # increasing
                        if not incr_start:
                            incr_start = idx
                            incr_value = 2
                        else:
                            incr_value += 1
                        total_candies += incr_value
        return total_candies

    def candy(self, ratings: List[int]) -> int:
        forward, backward = [0] * len(ratings), [0] * len(ratings)
        for idx in range(len(ratings)):
            if idx == 0:
                forward[idx] = 1
            else:
                if ratings[idx] > ratings[idx-1]:
                    forward[idx] = forward[idx-1] + 1
                else:
                    forward[idx] = 1
        for idx in range(len(ratings)-1, -1, -1):
            if idx == len(ratings)-1:
                backward[idx] = 1
            else:
                if ratings[idx] > ratings[idx+1]:
                    backward[idx] = backward[idx+1] + 1
                else:
                    backward[idx] = 1
        total = 0
        for idx in range(len(ratings)):
            total += max(forward[idx], backward[idx])
        return total

                            
        

'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    ([[1,0,2]], 5),
    ([[1,2,2]], 4),
    ([[1,3,2,2,1]], 7),
    ([[1,2,87,87,87,2,1]], 13),
    ([[5,4,3,2,1]], 15),
]

solution = Solution().candy

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
