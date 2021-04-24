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
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) < 1: return False
        if len(str1) != len(str2): return False
        if str1 == str2: return True

        char_map = dict()
        diff_char_same_mapping = dict()
        # check if same chars in str1 have different mapping in str2
        for idx, char in enumerate(str1):
            destination_char = str2[idx]
            if char not in char_map:
                char_map[char] = destination_char
                if destination_char not in diff_char_same_mapping:
                    diff_char_same_mapping[destination_char] = set()
                diff_char_same_mapping[destination_char].add(char)
            elif char_map[char] != destination_char:
                return False

        # check if different chars in source have same destination char
        for char_set in diff_char_same_mapping.values():
            if len(char_set) > 1:
                return True

        # check if there is any way to break the cycle
        cycle_exists = True
        for k, v in char_map.items():
            # if k == v or v not in char_map.keys():
            if v not in char_map.keys():
                cycle_exists = False
        # print(char_map)
        # if len(char_map) < 26
        return not cycle_exists or (cycle_exists and len(char_map) < 26)


            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["aabcc", "ccdee"], True),
        (["leetcode", "codeleet"], False),
        (["abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"], False),
        (["abcdefghijklmnopqrstuvwxy", "bcdefghijklmnopqrstuvwxyz"], True),
        (["abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyzz"], True),
        (["ab", "ba"], True),
        (["abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyzq"], True),
        (["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxzy"], False),
        (["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"], True),
    ]

    Tester.factory(test_cases, func=lambda input: sol.canConvert(*input)).run(unordered_output=False)
