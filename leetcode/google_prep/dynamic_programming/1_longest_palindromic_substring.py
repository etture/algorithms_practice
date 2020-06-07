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
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        center_pairs = list()
        limit = len(s)
        for start_idx in range(len(s)):
            if start_idx + 1 < limit:
                if s[start_idx] == s[start_idx + 1]:
                    center_pairs.append(tuple([start_idx, start_idx + 1]))
            if start_idx + 2 < limit:
                if s[start_idx] == s[start_idx + 2]:
                    center_pairs.append(tuple([start_idx, start_idx + 2]))

        if len(center_pairs) == 0:
            return s[0]

        max_len = 0
        max_palindrome = None
        for pair in center_pairs:
            start, end = pair
            start_, end_ = start, end
            length = end - start + 1
            increment = 1
            while True:
                before, after = start - increment, end + increment
                if before < 0 or after >= limit:
                    break
                if s[before] != s[after]:
                    break
                length += 2
                start_, end_ = before, after
                increment += 1
            if length > max_len:
                max_len = length
                max_palindrome = s[start_:end_ + 1]
        return max_palindrome
        

'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    (["babad"], "bab"),
    (["cbbd"], "bb"),
    ([""], ""),
    (["ac"], "a"),
    (["abcda"], "a")
]

solution = Solution().longestPalindrome

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
