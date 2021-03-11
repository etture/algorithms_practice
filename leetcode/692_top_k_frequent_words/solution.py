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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_map = dict()
        for word in words:
            if word not in count_map:
                count_map[word] = 0
            count_map[word] += 1
        sorted_list = sorted(count_map.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in sorted_list[:k]]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [["i", "love", "leetcode", "i", "love", "coding"], 2],
            ["i", "love"]
        ),
        (
            [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
            ["the", "is", "sunny", "day"]
        ),
        (
            [["the", "day", "is", "fry", "sunny", "the", "the", "the", "sunny", "is", "the", "the", "fry", "fry", "is", "fry"], 3],
            ["the", "fry", "is"]
        ),
        (
            [["the", "day", "is", "fry", "sunny", "the", "the", "the", "sunny", "is", "the", "the", "fry", "fry", "is", "fry"], 2],
            ["the", "fry"]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.topKFrequent(*input)).run(unordered_output=False)
