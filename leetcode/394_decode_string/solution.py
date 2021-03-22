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
    def decodeString(self, s: str) -> str:
        return self.recursive_construct(s, 0, 1)[0]

    def recursive_construct(self, whole: str, idx: int, multiplier: int):
        local_str = list()
        continue_idx = -1
        number_buffer = list()
        for i in range(idx, len(whole)):
            char = whole[i]
            if continue_idx > -1 and i < continue_idx:
                continue

            if char.isnumeric():
                number_buffer.append(char)
            elif char == '[':
                substr, continue_idx = self.recursive_construct(whole, i+1, int(''.join(number_buffer)))
                local_str.append(substr)
                number_buffer = list()
            elif char == ']':
                return ''.join(local_str) * multiplier, i+1
            else:
                local_str.append(char)
        return ''.join(local_str), len(whole)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["3[a]2[bc]"], "aaabcbc"),
        (["3[a2[c]]"], "accaccacc"),
        (["2[abc]3[cd]ef"], "abcabccdcdcdef"),
        (["abc3[cd]xyz"], "abccdcdcdxyz"),
        (["ab2[c3[c2[d]]x]y4[z]"], "abccddcddcddxccddcddcddxyzzzz"),
        (["100[leetcode]"], "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.decodeString(*input)).run(unordered_output=False)
