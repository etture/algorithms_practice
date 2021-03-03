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
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        if len(words) == 1:
            return 1
        dp = dict()
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                possible_predecessor = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp.get(possible_predecessor, 0) + 1)
        # print(dp.values())
        return max(dp.values())


    def longestStrChain_inefficient(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        if len(words) == 1:
            return 1

        # brute force
        def check_larger_has_smaller(larger, smaller) -> bool:
            if len(larger) - len(smaller) != 1:
                return False
            s_idx = 0
            # print(f'larger: {larger}, smaller: {smaller}')
            for l_char in larger:
                if s_idx >= len(smaller):
                    return True
                if l_char == smaller[s_idx]:
                    s_idx += 1
            return s_idx == len(smaller)

        words = sorted(words, key=lambda x: len(x))
        
        dict_by_length = dict()
        max_length = 0
        for word in words:
            length = len(word)
            max_length = max(max_length, length)
            if length not in dict_by_length:
                dict_by_length[length] = list()
            dict_by_length[length].append([word, 1])
        # print(dict_by_length)

        max_chain = 1

        for length in range(1, max_length):
            if length not in dict_by_length:
                continue
            if length + 1 not in dict_by_length:
                continue
            cur_list = dict_by_length[length]
            next_list = dict_by_length[length+1]
            for c in cur_list:
                for idx, n in enumerate(dict_by_length[length+1]):
                    if check_larger_has_smaller(n[0], c[0]):
                        length_so_far = max(c[1] + 1, dict_by_length[length+1][idx][1])
                        dict_by_length[length+1][idx][1] = length_so_far
                        max_chain = max(max_chain, length_so_far)

        # print(dict_by_length)
        # print(f'max_chain: {max_chain}')
        return max_chain

        


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[]], 0),
        ([["a","b","ba","bca","bda","bdca"]], 4),
        ([["xbc","pcxbcf","xb","cxbc","pcxbc"]], 5),
        ([["abcdef", "abcde", "abcd", "abc", "ab", "a"]], 6),
        ([["ababdb", "mnmnmn", "lr", "l", "trtrtr"]], 2),
        ([["a", "b", "c", "d"]], 1),
        ([["a","ab","ac","bd","abc","abd","abdd"]], 4),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestStrChain(*input)).run(unordered_output=False)
