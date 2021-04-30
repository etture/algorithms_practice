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
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def encoded(word: str) -> List[tuple]:
            prev_char = None
            cur_cnt = 0
            encoding = list()
            for char in word:
                if char == prev_char:
                    cur_cnt += 1
                else:
                    if prev_char is not None:
                        encoding.append((prev_char, cur_cnt))
                    prev_char = char
                    cur_cnt = 1
            encoding.append((prev_char, cur_cnt))
            return encoding
        
        total_expressive = 0
        given_encoded = encoded(S)
        for word in words:
            query_encoded = encoded(word)
            # print(f'given_encoded: {given_encoded}, query_encoded: {query_encoded}')
            if len(given_encoded) != len(query_encoded): continue
            match = True
            for i in range(len(query_encoded)):
                if query_encoded[i][0] != given_encoded[i][0] or given_encoded[i][1] < query_encoded[i][1] or (given_encoded[i][1] > query_encoded[i][1] and given_encoded[i][1] < 3):
                    match = False
                    break
            if match: 
                total_expressive += 1

        return total_expressive


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["heeellooo", ["hello", "hi", "helo"]], 1),
        (["heeellllllooo", ["hello", "hi", "helo"]], 2),
        (["hiiiii", ["hello", "hi", "helo"]], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.expressiveWords(*input)).run(unordered_output=False)
