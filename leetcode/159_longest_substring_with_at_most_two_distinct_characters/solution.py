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
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2: return len(s)

        pair_map = dict()
        last_idx_map = dict()
        start_idx, end_idx = 0, 0
        
        pair_map[s[start_idx]] = None
        last_idx_map[s[start_idx]] = start_idx

        max_len = cur_len = 1

        while end_idx + 1 < len(s):
            end_idx += 1
            cur_char = s[end_idx]
            if len(last_idx_map) < 2:
                pair_map[s[start_idx]] = cur_char
                pair_map[cur_char] = s[start_idx]
                cur_len += 1
            elif cur_char not in last_idx_map:  # new character
                prev_char = s[end_idx - 1]
                char_to_evict = pair_map[prev_char]
                start_idx = last_idx_map[char_to_evict] + 1
                del pair_map[char_to_evict]
                pair_map[cur_char] = prev_char
                pair_map[prev_char] = cur_char
                del last_idx_map[char_to_evict]
                last_idx_map[prev_char] = end_idx - 1
                cur_len = end_idx - start_idx + 1
            else:
                last_idx_map[cur_char] = end_idx
                cur_len += 1
            last_idx_map[cur_char] = end_idx
            max_len = max(max_len, cur_len)
            # print(f'start_idx: {start_idx}, end_idx: {end_idx}, cur_len: {cur_len}, max_len: {max_len}, pair_map: {pair_map}, last_idx_map: {last_idx_map}')

        return max_len



if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        (["eceba"], 3),
        (["ccaabbb"], 5),
        (["ababababc"], 8),
        (["ababcbabc"], 4),
        (["eceba"], 3),
        (["ababffzzeee"], 5),
    ]
    Tester.factory(test_cases, func=lambda input: sol.lengthOfLongestSubstringTwoDistinct(*input)).run(unordered_output=False)
