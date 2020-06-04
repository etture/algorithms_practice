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
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        start_idx, end_idx = 0, -1
        cur_len, max_len = 0, 0
        cur_char_idx = dict()
        while end_idx < len(s)-1:
            end_idx += 1
            if start_idx == end_idx:
                cur_len = 1
                cur_char_idx[s[end_idx]] = end_idx
            else:
                char = s[end_idx]
                # print(f'start: {start_idx}, end: {end_idx}, '
                #       f'substring: {s[start_idx:end_idx]}, char: {char}, '
                #       f'cur_char_idx: {cur_char_idx}')
                if char in cur_char_idx:
                    start_idx = cur_char_idx[char] + 1
                    chars_to_delete = list()
                    for c in cur_char_idx:
                        if cur_char_idx[c] < start_idx:
                            chars_to_delete.append(c)
                    for c in chars_to_delete:
                        del cur_char_idx[c]
                    cur_char_idx[char] = end_idx
                    # print(f'     cur_char_idx: {cur_char_idx}')
                    cur_len = end_idx - start_idx + 1
                else:
                    cur_char_idx[char] = end_idx
                    cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len



            


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    (["abcabcbb"], 3),
    (["bbbbb"], 1),
    (["pwwkew"], 3),
    (["annnmkilopwerfaaaaaaabnmqq"], 12),
    ([" "], 1),
    (["a"], 1),
    (["asjrgapa"], 6)
]

solution = Solution().lengthOfLongestSubstring

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
