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
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) <= 0: return 0
        if len(haystack) <= 0: return -1
        if len(needle) > len(haystack): return -1
        kmp_table = self.construct_lps_table(needle)
        # print(f'table: {kmp_table}')

        i, j = 0, 0
        while True:
            # print(f'i: {i}, j: {j}')
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = kmp_table[j-1]
                else:
                    i += 1

            if j >= len(needle):
                return i - len(needle)
            if i >= len(haystack):
                return -1
            


    def construct_lps_table(self, pattern: str) -> List[int]:
        # print(f'pattern: {pattern}')
        table = list()
        i = 0
        length = 0
        table_completed = False
        while not table_completed:
            if i == 0: 
                table.append(length)
                i += 1
            else:
                if pattern[i] == pattern[length]:
                    length += 1
                    table.append(length)
                    i += 1
                elif length > 0:
                    length = table[length-1]
                else:
                    table.append(length)
                    i += 1
            # print(f'idx: {i}, table: {table}')

            if len(table) >= len(pattern):
                table_completed = True
        # print(f'final table: {table}')
        return table
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["hello", "ll"], 2),
        (["aaaaa", "bba"], -1),
        (["aaaaa", ""], 0),
        (["", ""], 0),
        (["mississippi", "issip"], 4),
        (["", "a"], -1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.strStr(*input)).run(unordered_output=False)
