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
    def decodeString(self, s: str) -> str:
        def traverse(idx: int) -> tuple(str, int):  # return base string and next idx in s
            tmp_str = ''
            cur_multipler_str = ''
            while idx < len(s):
                # print(f'tmp_str: {tmp_str}')
                if s[idx].isalpha():
                    tmp_str += s[idx]
                    idx += 1
                elif s[idx].isnumeric():
                    cur_multipler_str += s[idx]
                    if s[idx+1].isnumeric():
                        idx += 1
                        continue
                    multiplier = int(cur_multipler_str)
                    cur_multipler_str = ''
                    base_str, next_idx = traverse(idx+2)
                    tmp_str += multiplier * base_str
                    # print(f' numeric, multiplier: {multiplier}, base_str: {base_str}')
                    idx = next_idx
                elif s[idx] == ']':
                    # print(f'  returning -> {tmp_str}')
                    return tmp_str, idx+1
            return tmp_str, -1
        return traverse(0)[0]





test_cases = [
    (["3[a]2[bc]"], "aaabcbc"),
    (["3[a2[c]]"], "accaccacc"),
    (["2[abc]3[cd]ef"], "abcabccdcdcdef"),
    (["abc3[cd]xyz"], "abccdcdcdxyz"),
    (["ab2[c3[c2[d]]x]y4[z]"], "abccddcddcddxccddcddcddxyzzzz"),
    (["100[leetcode]"], "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.decodeString(*input)).run(unordered_output=False)
