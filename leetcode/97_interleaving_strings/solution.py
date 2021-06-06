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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1 + s2): return False

        backtrack_map = dict()
        terminal_1, terminal_2 = len(s1), len(s2)
        def backtrack(_idx_1: int, _idx_2: int, s3_idx: int) -> bool:
            if s3_idx >= len(s3): return True
            
            # memoization
            key = tuple([_idx_1, _idx_2, s3_idx])
            if key in backtrack_map:
                return backtrack_map[key]

            cur_char = s3[s3_idx]
            idx_1_possible, idx_2_possible = False, False
            if _idx_1 < terminal_1 and s1[_idx_1] == cur_char and backtrack(_idx_1 + 1, _idx_2, s3_idx + 1):
                backtrack_map[key] = True
                return True
            if _idx_2 < terminal_2 and s2[_idx_2] == cur_char and backtrack(_idx_1, _idx_2 + 1, s3_idx + 1):
                backtrack_map[key] = True
                return True
            backtrack_map[key] = False
            return False

        return backtrack(0, 0, 0)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["aabcc", "dbbca", "aadbbcbcac"], True),
        (["aabcc", "dbbca", "aadbbbaccc"], False),
        (["", "", ""], True),
        (["cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
        "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
        "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"], True),
        (["bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"], False),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isInterleave(*input)).run(unordered_output=False)
