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
    def countAndSay(self, n: int) -> str:
        say = "1"
        for _ in range(1, n):
            cur_num = -1
            buckets = list()
            for num in [int(char) for char in say]:
                if num != cur_num:
                    buckets.append([num, 1])
                    cur_num = num
                else:
                    buckets[-1][1] += 1
            say = "".join([str(b[1]) + str(b[0]) for b in buckets])
            # print(buckets)
            # print(say)
        return say



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([1], "1"),
        ([2], "11"),
        ([3], "21"),
        ([4], "1211"),
        ([5], "111221"),
        ([6], "312211"),
        ([7], "13112221"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.countAndSay(*input)).run(unordered_output=False)
