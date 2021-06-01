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
    def numSplits(self, s: str) -> int:
        # naive way
        # cnt = 0
        # for idx in range(1, len(s)):
        #     if len(set(s[:idx])) == len(set(s[idx:])):
        #         cnt += 1
        # return cnt

        # more efficient way
        cnt = 0
        left_set, right_set = dict(), dict()
        for idx in range(1, len(s)):
            if idx == 1:
                for elem in s[:idx]:
                    if elem not in left_set:
                        left_set[elem] = 0
                    left_set[elem] += 1
                for elem in s[idx:]:
                    if elem not in right_set:
                        right_set[elem] = 0
                    right_set[elem] += 1
            else:
                elem = s[idx-1]
                if elem not in left_set:
                    left_set[elem] = 0
                left_set[elem] += 1

                right_set[elem] -= 1
                if right_set[elem] <= 0:
                    del right_set[elem]
            # print(f'idx: {idx}, left: {left_set}, right: {right_set}')
            if len(left_set) == len(right_set):
                cnt += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["aacaba"], 2),
        (["abcd"], 1),
        (["aaaaa"], 4),
        (["acbadbaada"], 2),
    ]

    Tester.factory(test_cases, func=lambda input: sol.numSplits(*input)).run(unordered_output=False)
